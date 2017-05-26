# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import google.cloud.proto.devtools.cloudtrace.v1.trace_pb2 as google_dot_cloud_dot_proto_dot_devtools_dot_cloudtrace_dot_v1_dot_trace__pb2
import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2


class TraceServiceStub(object):
  """This file describes an API for collecting and viewing traces and spans
  within a trace.  A Trace is a collection of spans corresponding to a single
  operation or set of operations for an application. A span is an individual
  timed event which forms a node of the trace tree. Spans for a single trace
  may span multiple services.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListTraces = channel.unary_unary(
        '/google.devtools.cloudtrace.v1.TraceService/ListTraces',
        request_serializer=google_dot_cloud_dot_proto_dot_devtools_dot_cloudtrace_dot_v1_dot_trace__pb2.ListTracesRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_proto_dot_devtools_dot_cloudtrace_dot_v1_dot_trace__pb2.ListTracesResponse.FromString,
        )
    self.GetTrace = channel.unary_unary(
        '/google.devtools.cloudtrace.v1.TraceService/GetTrace',
        request_serializer=google_dot_cloud_dot_proto_dot_devtools_dot_cloudtrace_dot_v1_dot_trace__pb2.GetTraceRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_proto_dot_devtools_dot_cloudtrace_dot_v1_dot_trace__pb2.Trace.FromString,
        )
    self.PatchTraces = channel.unary_unary(
        '/google.devtools.cloudtrace.v1.TraceService/PatchTraces',
        request_serializer=google_dot_cloud_dot_proto_dot_devtools_dot_cloudtrace_dot_v1_dot_trace__pb2.PatchTracesRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class TraceServiceServicer(object):
  """This file describes an API for collecting and viewing traces and spans
  within a trace.  A Trace is a collection of spans corresponding to a single
  operation or set of operations for an application. A span is an individual
  timed event which forms a node of the trace tree. Spans for a single trace
  may span multiple services.
  """

  def ListTraces(self, request, context):
    """Returns of a list of traces that match the specified filter conditions.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTrace(self, request, context):
    """Gets a single trace by its ID.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PatchTraces(self, request, context):
    """Sends new traces to Stackdriver Trace or updates existing traces. If the ID
    of a trace that you send matches that of an existing trace, any fields
    in the existing trace and its spans are overwritten by the provided values,
    and any new fields provided are merged with the existing trace data. If the
    ID does not match, a new trace is created.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TraceServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListTraces': grpc.unary_unary_rpc_method_handler(
          servicer.ListTraces,
          request_deserializer=google_dot_cloud_dot_proto_dot_devtools_dot_cloudtrace_dot_v1_dot_trace__pb2.ListTracesRequest.FromString,
          response_serializer=google_dot_cloud_dot_proto_dot_devtools_dot_cloudtrace_dot_v1_dot_trace__pb2.ListTracesResponse.SerializeToString,
      ),
      'GetTrace': grpc.unary_unary_rpc_method_handler(
          servicer.GetTrace,
          request_deserializer=google_dot_cloud_dot_proto_dot_devtools_dot_cloudtrace_dot_v1_dot_trace__pb2.GetTraceRequest.FromString,
          response_serializer=google_dot_cloud_dot_proto_dot_devtools_dot_cloudtrace_dot_v1_dot_trace__pb2.Trace.SerializeToString,
      ),
      'PatchTraces': grpc.unary_unary_rpc_method_handler(
          servicer.PatchTraces,
          request_deserializer=google_dot_cloud_dot_proto_dot_devtools_dot_cloudtrace_dot_v1_dot_trace__pb2.PatchTracesRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.devtools.cloudtrace.v1.TraceService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
