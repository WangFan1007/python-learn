
from gevent import monkey;monkey.patch_all()

import socket
import gevent

def chat(conn):
    conn.send(b'Hello')
    msg = conn.recv(1024)
    print(msg.decode('utf-8'))
    conn.close()


sk = socket.socket()
sk.bind(('127.0.0.1',8080))

sk.listen()

while True:
    conn,addr = sk.accept()
    gevent.spawn(chat,conn)