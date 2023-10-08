import threading
from client import simple_client
from server import echo_server

HOST = '127.0.0.1'
PORT = 5555

serv = threading.Thread(target=echo_server, args=(HOST, PORT))
clie = threading.Thread(target=simple_client, args=(HOST, PORT))

serv.start()
clie.start()

serv.join()
clie.join()

print('DONE!')