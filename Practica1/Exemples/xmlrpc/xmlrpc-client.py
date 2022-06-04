import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')

print(proxy.addInsult('Moc'))
print(proxy.getInsults())
print(proxy.insultme())