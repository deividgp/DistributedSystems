from io import StringIO
import xmlrpc.client
import pandas
import redis
import json
import time

def addWorkers():
    global workers
    workers = []
    for address in addresses:
        workers.append(xmlrpc.client.ServerProxy(address))

def hnd(msg):
    global workers, addresses
    aux = addresses
    addresses = json.loads(msg["data"])
    while busy:
        time.sleep(0.5)

    addWorkers()

    if len(addresses) < len(aux):
        diff = list(set(aux).difference(addresses))
        print("Removed workers:")
        print(diff)

    print(addresses)


red = redis.Redis('localhost', 6379, charset="utf-8", decode_responses=True)
master = xmlrpc.client.ServerProxy('http://localhost:9000')
num = 0
busy = False

addresses = master.getWorkers()
addWorkers()

p = red.pubsub()
p.subscribe(**{'workers': hnd})
thread = p.run_in_thread(sleep_time=0.001)

try:
    while (num != 10):
        print('\n1. List Workers')
        print('2. Apply A Function Along An Axis Of The DataFrame')
        print('3. Read Columns Labels')
        print('4. Group DataFrame By Columns')
        print('5. Read X Number Of Rows')
        print('6. Check Whether Each Element In The DataFrame Is Contained In Values')
        print('7. Iterate Over The DataFrame Columns')
        print('8. Get The Maximum Of The Values Over The Requested Column')
        print('9. Get The Minimum Of The Values Over The Requested Column.')
        print('10. Exit\n')
        num = int(input("Choose an option: "))
        result = []
        busy = True
        match num:
            case 1:
                try:
                    addresses = master.getWorkers()
                    result = addresses
                    addWorkers()
                except:
                    result = "Error"
            case 2:
                try:
                    func = input("Function To Apply Required: ")
                    label = input("Label Is Required: ")
                    for worker in workers:
                        result.append(worker._ServerProxy__host)
                        result.append(worker.apply(func, label))
                    prntRsults = input(
                        "Print Or Save In A File The Results(print/save)? ")
                    if (prntRsults == "save"):
                        with open(r'./ApplyResults.txt', 'w') as fp:
                            for item in result:
                                fp.write("%s\t\n" % item)
                        result = "File Saved"
                except:
                    result = "Error"
            case 3:
                try:
                    for worker in workers:
                        result.append(worker._ServerProxy__host)
                        result.append(worker.columns())
                except:
                    result = "Error"
            case 4:
                try:
                    by = input("Label Is Required: ")
                    op = input("Order By Mean or Sum (mean/sum): ")
                    for worker in workers:
                        result.append(worker.groupby(by, op))
                    df = None
                    for csv in result:
                        csvStringIO = StringIO(csv)
                        aux = pandas.read_csv(csvStringIO, sep=",", header=0)
                        df = pandas.concat([df, aux])
                    if (op == "mean"):
                        result = df.groupby(by).mean()
                    else:
                        result = df.groupby(by).sum()
                    prntRsults = input(
                        "Print Or Save In A File The Results(print/save)? ")
                    if (prntRsults == "save"):
                        result.to_csv("./OrderByResults.csv")
                        result = "File Saved"
                except:
                    result = "Error"
            case 5:
                try:
                    numRows = input("Number Of Rows Required: ")
                    for worker in workers:
                        result.append(worker._ServerProxy__host)
                        result.append(worker.head(int(numRows)))
                except:
                    result = "Error"
            case 6:
                try:
                    label = input("Column Label Required: ")
                    values = input("Values Required (Ex:0 2): ")
                    valList = values.split()
                    for worker in workers:
                        result.append(worker._ServerProxy__host)
                        result.append(worker.isin(valList[0], valList[1], label))
                    prntRsults = input(
                        "Print Or Save In A File The Results(print/save)? ")
                    if (prntRsults == "save"):
                        with open(r'./IsinResults.txt', 'w') as fp:
                            for item in result:
                                fp.write("%s\t\n" % item)
                        result = "File Saved"
                except:
                    result = "Error"
            case 7:
                try:
                    label = input("Column Label Required: ")
                    for worker in workers:
                        result.append(worker._ServerProxy__host)
                        result.append(worker.items(label))
                    prntRsults = input(
                        "Print Or Save In A File The Results(print/save)? ")
                    if (prntRsults == "save"):
                        with open(r'./ItemsResults.txt', 'w') as fp:
                            for item in result:
                                fp.write("%s\t\n" % item)
                        result = "File Saved"
                except:
                    result = "Error"
            case 8:
                try:
                    label = input("Column Label Required: ")
                    for worker in workers:
                        result.append(worker.max(label))
                    result = max(result)
                except:
                    result = "Error"
            case 9:
                try:
                    label = input("Column Label Required: ")
                    for worker in workers:
                        result.append(worker.min(label))
                    result = min(result)
                except:
                    result = "Error"
            case 10:
                result = "Have A Nice Day!"
        busy = False
        print(result)
        input("Press Enter To Continue...")
except KeyboardInterrupt:
    print('Exiting')
finally:
    thread.stop()
