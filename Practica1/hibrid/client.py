from asyncio.windows_events import NULL
from doctest import master
from traceback import format_exc
from io import StringIO
import xmlrpc.client
import pandas
import redis

red = redis.Redis('localhost', 6379, charset="utf-8", decode_responses=True)
workers = []
num = 0
workers = red.smembers("workers")
print(workers)

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
            workers = red.smembers("workers")
            result = workers
        case 2:
            func = input("Function To Apply Required: ")
            print("hola")
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
                result.to_csv("OrderByResults.csv")
                result = "File Saved"
        case 5:
            numRows = input("Number Of Rows Required: ")
            for worker in workers:
                result.append(worker._ServerProxy__host)
                result.append(worker.head(int(numRows)))
        case 6:
            values = input("Values Required (Ex:0 2): ")
            valList = values.split()
            for worker in workers:
                result.append(worker._ServerProxy__host)
                result.append(worker.isin(valList[0], valList[1]))
        case 7:
            nameFile = input("Name File Required: ")
            print("hola")
        case 8:
            label = input("Column Label Reuqired: ")
            nameFile = input("Name File Required: ")
            print("hola")
        case 9:
            label = input("Column Label Reuqired: ")
            nameFile = input("Name File Required: ")
            print("hola")
        case 10:
            result = "Have A Nice Day!"

    print(result)
    input("Press Enter To Continue...")
