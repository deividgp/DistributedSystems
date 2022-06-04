import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')

aux = 7
print('WORKER 1 CREATED')
print(proxy.createWorker())

while (aux != -1):
    print('\n1. Create Worker')
    print('2. List Workers')
    print('3. Delete Worker')
    print('4. Read CSV')
    print('5. Apply')
    print('6. Columns')
    print('7. Group By')
    print('8. Head')
    print('9. Isin')
    print('10. Items')
    print('11. Max')
    print('12. Min')
    print('13. Exit\n')
    num = int(input("Choose an option: "))

    aux = 0
    if (num == 1): aux = proxy.createWorker()
    if (num == 2): aux = proxy.listWorker()
    if (num == 3): 
        quin = int(input("ELIMINAR ID worker:"))
        aux = proxy.deleteWorker(quin)

    if (num == 13): aux = -1
    print(aux)