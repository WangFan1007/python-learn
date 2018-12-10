import socket

from multiprocessing import Process

def serve(conn):
    conn.send('欢迎'.encode('utf-8'))
    msg = conn.recv(1024).decode('utf-8')
    print(msg)
    conn.close()



sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sk.bind(('127.0.0.1',8080))

sk.listen()
while True:
    conn,addr = sk.accept()
    # conn.send('欢迎'.encode('utf-8'))
    # msg = conn.recv(1024).decode('utf-8')
    # print(msg)
    # conn.close()
    p = Process(target=serve,args=(conn,))
    p.start()

sk.close()