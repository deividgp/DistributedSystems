import grpc
from concurrent import futures
import time

import master_pb2
import master_pb2_grpc

workers = []


class MasterServicer(master_pb2_grpc.MasterServicer):
    """Missing associated documentation comment in .proto file."""

    def addWorker(self, address, context):
        addressAux = address.value
        response = master_pb2.Confirmation()
        response.value = False
        if addressAux != "9000" and addressAux not in workers:
            workers.append(addressAux)
            response.value = True
            print(workers)
        return response

    def deleteWorker(self, address, context):
        workers.remove(address.value)
        response = master_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

    def getWorkers(self, empty, context):
        response = master_pb2.Addresses()
        response.value.extend(workers)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

master_pb2_grpc.add_MasterServicer_to_server(
    MasterServicer(), server)

print('Starting server. Listening on port 9000.')
server.add_insecure_port('localhost:9000')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
