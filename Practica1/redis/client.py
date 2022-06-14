from io import StringIO
import pandas
from pkg_resources import resource_exists
import redis
import string
import random
import time


def generateListName():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


red = redis.Redis('localhost', 6379, charset="utf-8", decode_responses=True)
num = 0

while (num != 9):
    print('\n1. Apply A Function Along An Axis Of The DataFrame')
    print('2. Read Columns Labels')
    print('3. Group DataFrame Using A Mapper Or By A Series Of Columns')
    print('4. Read X Number Of Rows')
    print('5. Check Whether Each Element In The DataFrame Is Contained In Values')
    print('6. Iterate Over The DataFrame Columns')
    print('7. Get The Maximum Of The Values Over The Requested Column')
    print('8. Get The Minimum Of The Values Over The Requested Column.')
    print('9. Exit\n')
    num = int(input("Choose an option: "))

    result = ""
    params = ""
    if num != 9:
        listName = generateListName()

    match num:
        case 1:
            func = input("Function To Apply Required: ")
            label = input("Label Is Required: ")
            params = func + "," + label
            red.publish("functions", "apply:"+listName+":"+params)
            time.sleep(2)
            results=[]
            while (True):
                elem = red.lpop(listName)
                if (elem == None):
                    break
                else:
                    results.append(elem)
            prntRsults = input(
                "Print Or Save In A File The Results(print/save)? ")
            if (prntRsults == "save"):
                with open(r'./ApplyResults.csv', 'w') as fp:
                    for item in results:
                        fp.write("%s" % item)
                result = "File Saved"
        case 2:
            red.publish("functions", "columns:"+listName+":"+params)
            time.sleep(2)
            while (True):
                elem = red.lpop(listName)
                if (elem == None):
                    break
                else:
                    result = result + elem + "\n"
        case 3:
            by = input("Label Is Required: ")
            op = input("Order By Mean or Sum (mean/sum): ")
            params = by + "," + op
            red.publish("functions", "groupby:"+listName+":"+params)
            time.sleep(2)
            allCsv = []
            while (True):
                elem = red.lpop(listName)
                if (elem == None):
                    break
                else:
                    allCsv.append(elem)
            df = None
            for csv in allCsv:
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
        case 4:
            params = input("Number Of Rows Required: ")
            red.publish("functions", "head:"+listName+":" + params + ",")
            time.sleep(2)
            while (True):
                elem = red.lpop(listName)
                if (elem == None):
                    break
                else:
                    result = result + elem + "\n"
        case 5:
            label = input("Column Label Required: ")
            values = input("Values Required (Ex:0 2): ")
            valList = values.split()
            params = valList[0] + "," + valList[1] + "," + label
            red.publish("functions", "isin:"+listName+":"+params)
            time.sleep(2)
            while (True):
                elem = red.lpop(listName)
                if (elem == None):
                    break
                else:
                    result = result + elem
            prntRsults = input(
                "Print Or Save In A File The Results(print/save)? ")
            if (prntRsults == "save"):
                with open(r'./IsinResults.csv', 'w') as fp:
                    fp.write("%s" % result)
                result = "File Saved"
        case 6:
            label = input("Column Label Required: ")
            params = label + ","
            red.publish("functions", "items:"+listName+":"+params)
            time.sleep(10)
            while (True):
                elem = red.lpop(listName)
                if (elem == None):
                    break
                else:
                    result = result + elem
            prntRsults = input(
                "Print Or Save In A File The Results(print/save)? ")
            if (prntRsults == "save"):
                with open(r'./ItemsResults.txt', 'w') as fp:
                    fp.write("%s" % result)
                result = "File Saved"
        case 7:
            label = input("Column Label Required: ")
            params = label + ","
            red.publish("functions", "max:"+listName+":"+params)
            time.sleep(5)
            results = []
            while (True):
                elem = red.lpop(listName)
                if (elem == None):
                    break
                else:
                    results.append(elem)
            result = max(results)
        case 8:
            label = input("Column Label Required: ")
            params = label + ","
            red.publish("functions", "min:"+listName+":"+params)
            time.sleep(5)
            results = []
            while (True):
                elem = red.lpop(listName)
                if (elem == None):
                    break
                else:
                    results.append(elem)
            result = min(results)
        case 9:
            result = "Have A Nice Day!"
    print(result)
    input("Press Enter To Continue...")
