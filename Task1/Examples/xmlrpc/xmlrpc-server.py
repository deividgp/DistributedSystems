from xmlrpc.server import SimpleXMLRPCServer
import logging
from InsultingService import insultingService

logging.basicConfig(level=logging.INFO)

server = SimpleXMLRPCServer(
    ('0.0.0.0', 9000),
    logRequests=True
)

server.register_instance(insultingService)

try:
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
