from doctest import master
import grpc
import worker_pb2
import worker_pb2_grpc
import master_pb2
import master_pb2_grpc

channel = grpc.insecure_channel('localhost:9000')
master = master_pb2_grpc.MasterStub(channel)
workers = []
num = 0
response = master.getWorkers(
    master_pb2.google_dot_protobuf_dot_empty__pb2.Empty())
result = response.value
for address in response.value:
    workers.append(worker_pb2_grpc.WorkerStub(grpc.insecure_channel(address)))

while (num != 4):
    print('\n1. List & Update Workers')
    print('2. Get The Maximum Of The Values Over The Requested Column')
    print('3. Get The Minimum Of The Values Over The Requested Column.')
    print('4. Exit\n')
    num = int(input("Choose an option: "))
    result = []
    match num:
        case 1:
            workers = []
            response = master.getWorkers(
                master_pb2.google_dot_protobuf_dot_empty__pb2.Empty())
            result = response.value
            for address in response.value:
                workers.append(worker_pb2_grpc.WorkerStub(
                    grpc.insecure_channel(address)))
        case 2:
            label = input("Column Label Required: ")
            for worker in workers:
                result.append(worker.max(worker_pb2.Label(value=label)))
            result = max(result)
        case 3:
            label = input("Column Label Required: ")
            for worker in workers:
                result.append(worker.min(worker_pb2.Label(value=label)))
            result = min(result)
        case 4:
            result = "Have A Nice Day!"

    print(result)
    input("Press Enter To Continue...")
