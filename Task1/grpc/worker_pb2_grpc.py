# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import worker_pb2 as worker__pb2


class WorkerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.max = channel.unary_unary(
                '/Worker/max',
                request_serializer=worker__pb2.Label.SerializeToString,
                response_deserializer=worker__pb2.Response.FromString,
                )
        self.min = channel.unary_unary(
                '/Worker/min',
                request_serializer=worker__pb2.Label.SerializeToString,
                response_deserializer=worker__pb2.Response.FromString,
                )


class WorkerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def max(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def min(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'max': grpc.unary_unary_rpc_method_handler(
                    servicer.max,
                    request_deserializer=worker__pb2.Label.FromString,
                    response_serializer=worker__pb2.Response.SerializeToString,
            ),
            'min': grpc.unary_unary_rpc_method_handler(
                    servicer.min,
                    request_deserializer=worker__pb2.Label.FromString,
                    response_serializer=worker__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Worker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Worker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def max(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Worker/max',
            worker__pb2.Label.SerializeToString,
            worker__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def min(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Worker/min',
            worker__pb2.Label.SerializeToString,
            worker__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
