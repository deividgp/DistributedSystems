import grpc

# import the generated classes
import insultingServer_pb2
import insultingServer_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = insultingServer_pb2_grpc.InsultingServiceStub(channel)

# create a valid request message
insult = insultingServer_pb2.Insult(value='Moc')
stub.addInsult(insult)

insult = insultingServer_pb2.Insult(value='Mocoloco')
stub.addInsult(insult)

insult = insultingServer_pb2.Insult(value='Mocoloquito')
stub.addInsult(insult)

# create a valid request message
empty = insultingServer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
response = stub.getInsults(empty)
print(response.value)


# create a valid request message
empty = insultingServer_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
response = stub.insultme(empty)
print(response.value)