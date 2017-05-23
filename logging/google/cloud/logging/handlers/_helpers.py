# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Helper functions for logging handlers."""

import math
import json
import sys

try:
    import flask
except ImportError:
    flask = None

from google.cloud.logging.handlers.middleware.request import get_request


def format_stackdriver_json(record, message):
    """Helper to format a LogRecord in in Stackdriver fluentd format.

        :rtype: str
        :returns: JSON str to be written to the log file.
    """
    subsecond, second = math.modf(record.created)

    payload = {
        'message': message,
        'timestamp': {
            'seconds': int(second),
            'nanos': int(subsecond * 1e9),
        },
        'thread': record.thread,
        'severity': record.levelname,
    }

    return json.dumps(payload)


def detect_web_framework():
    """Detect web framework used in this environment.

    Detect which web framework is used by looking at the sys.modules.
    If multiple or no supported web frameworks detected in the modules, then
    print a warning message.
    Return the name of web framework detected if flask or django is found.
    Return unknown if cannot determine.

    :rtype: str
    :returns: Web framework detected in this environment.
    """
    modules = sys.modules
    web_framework = 'unknown'

    if 'flask' in modules and 'django' in modules:
        print('Cannot determine, found multiple web frameworks.')
    elif 'flask' in modules:
        web_framework = 'flask'
    elif 'django' in modules:
        web_framework = 'django'
    else:
        print('No supported web framework found in the modules.')
    return web_framework


def get_trace_id_from_request_header():
    """Helper to get trace_id from web application request header.

    :rtype: str
    :returns: Trace_id in HTTP request headers.
    """
    web_framework = detect_web_framework()

    if web_framework is 'flask':
        try:
            trace_id = flask.request.headers['X_CLOUD_TRACE_CONTEXT'].split('/')[0]
        except Exception:
            trace_id = None
    elif web_framework is 'django':
        try:
            request = get_request()
            trace_id = request.META['HTTP_X_CLOUD_TRACE_CONTEXT'].split('/')[0]
        except Exception:
            trace_id = None
    else:
        trace_id = None
    return trace_id
