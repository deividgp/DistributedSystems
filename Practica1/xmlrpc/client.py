import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')

aux = 0
print('One Worker Created')
print(proxy.createWorker())

while (aux != -1):
    print('\n1. Create Worker')
    print('2. List Workers')
    print('3. Delete Worker')
    print('4. Read CSV')
    print('5. Apply A Function Along An Axis Of The DataFrame')
    print('6. Read Columns Labels')
    print('7. Group DataFrame Using A Mapper Or By A Series Of Columns')
    print('8. Read X Number Of Rows')
    print('9. Check Whether Each Element In The DataFrame Is Contained In Values')
    print('10. Iterate Over The DataFrame Columns')
    print('11. Get The Maximum Of The Values Over The Requested Column')
    print('12. Get The Minimum Of The Values Over The Requested Column.')
    print('13. Exit\n')
    num = int(input("Choose an option: "))

    match num:
        case 1:
            result = proxy.createWorker()
        case 2:
            result = proxy.listWorker()
        case 3:
            idWorker = int(input("Worker ID Required: "))
            result = proxy.deleteWorker(idWorker)
        case 4:
            filePath = input("File Path Required: ")
            result = proxy.read_csv(filePath)
        case 5:
            func = input("Function To Apply Required: ")
            nameFile = input("Name File Required: ")
            result = proxy.apply(func,nameFile)
        case 6: 
            nameFile = input("Name File Required: ")
            result = proxy.columns(nameFile)
        case 7:
            by = input("Mapping, Function, Label Or List Of Labels Is Required")
            nameFile = input("Name File Required: ")
            result = proxy.groupby(by, nameFile)
        case 8:
            numRows = input("Number Of Rows Required: ")
            nameFile = input("Name File Required: ")
            result = proxy.head(numRows, nameFile)
        case 9:
            values = input("Values Required (Iterable, Series, DataFrame Or Dict): ")
            nameFile = input("Name File Required: ")
            result = proxy.isin(values, nameFile)
        case 10:
            nameFile = input("Name File Required: ")
            result = proxy.items(nameFile)
        case 11:
            label = input("Column Label Reuqired: ")
            nameFile = input("Name File Required: ")
            result = proxy.max(label, nameFile)
        case 12:
            label = input("Column Label Reuqired: ")
            nameFile = input("Name File Required: ")
            result = proxy.min(label, nameFile)
        case 13:
            aux = -1
            result = "Have A Nice Day!"

    print(result)