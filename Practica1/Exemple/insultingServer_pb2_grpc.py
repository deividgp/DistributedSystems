# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import insultingServer_pb2 as insultingServer__pb2


class InsultingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getInsults = channel.unary_unary(
                '/InsultingService/getInsults',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=insultingServer__pb2.Insults.FromString,
                )
        self.addInsult = channel.unary_unary(
                '/InsultingService/addInsult',
                request_serializer=insultingServer__pb2.Insult.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.insultme = channel.unary_unary(
                '/InsultingService/insultme',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=insultingServer__pb2.Insult.FromString,
                )


class InsultingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getInsults(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def addInsult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def insultme(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InsultingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getInsults': grpc.unary_unary_rpc_method_handler(
                    servicer.getInsults,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=insultingServer__pb2.Insults.SerializeToString,
            ),
            'addInsult': grpc.unary_unary_rpc_method_handler(
                    servicer.addInsult,
                    request_deserializer=insultingServer__pb2.Insult.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'insultme': grpc.unary_unary_rpc_method_handler(
                    servicer.insultme,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=insultingServer__pb2.Insult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'InsultingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InsultingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getInsults(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InsultingService/getInsults',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            insultingServer__pb2.Insults.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def addInsult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InsultingService/addInsult',
            insultingServer__pb2.Insult.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def insultme(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InsultingService/insultme',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            insultingServer__pb2.Insult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
