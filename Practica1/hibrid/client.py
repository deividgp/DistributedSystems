from io import StringIO
import xmlrpc.client
import pandas
import redis

red = redis.Redis('localhost', 6379, charset="utf-8", decode_responses=True)
workers = []
num = 0
workers = red.smembers("workers")

while (num != 10):
    print('\n1. List & Update Workers')
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
    match num:
        case 1:
            result = red.smembers("workers")
            for address in result:
                workers.append(xmlrpc.client.ServerProxy(address))
        case 2:
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
        case 3:
            for worker in workers:
                result.append(worker._ServerProxy__host)
                result.append(worker.columns())
        case 4:
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
        case 5:
            numRows = input("Number Of Rows Required: ")
            for worker in workers:
                result.append(worker._ServerProxy__host)
                result.append(worker.head(int(numRows)))
        case 6:
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
        case 7:
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
        case 8:
            label = input("Column Label Required: ")
            for worker in workers:
                result.append(worker.max(label))
            result = max(result)
        case 9:
            label = input("Column Label Required: ")
            for worker in workers:
                result.append(worker.min(label))
            result = min(result)
        case 10:
            result = "Have A Nice Day!"

    print(result)
    input("Press Enter To Continue...")
