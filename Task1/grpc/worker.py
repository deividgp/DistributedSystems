import pandas
import sys
import grpc
from concurrent import futures
import time
import master_pb2
import master_pb2_grpc
import worker_pb2
import worker_pb2_grpc

df = ""


def read_csv(route):
    global df
    df = pandas.read_csv(route)


class WorkerServicer(worker_pb2_grpc.WorkerServicer):
    """Missing associated documentation comment in .proto file."""

    def max(self, label, context):
        response = worker_pb2.Response()
        response.value = str(df[label.value].max())
        return response

    def min(self, label, context):
        response = worker_pb2.Response()
        response.value = str(df[label.value].min())
        return response


address = "localhost:"+sys.argv[1]

channel = grpc.insecure_channel('localhost:9000')
stub = master_pb2_grpc.MasterStub(channel)

route = input("CSV route: ")
read_csv(route)

response = stub.addWorker(master_pb2.Address(value=address))
created = response.value

if created:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    worker_pb2_grpc.add_WorkerServicer_to_server(
        WorkerServicer(), server)

    print('Starting server. Listening on port ', sys.argv[1])
    server.add_insecure_port(address)
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        stub.deleteWorker(master_pb2.Address(value=address))
        server.stop(0)
        print('Exiting')
else:
    print("worker with address " + address+" could not be created")
