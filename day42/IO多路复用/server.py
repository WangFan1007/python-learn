
import select
import socket


sk = socket.socket()
sk.setblocking(False)

sk.bind(('127.0.0.1',8080))
sk.listen()

read_lst = [sk]

while True:
    r_lst,w_lst,x_lst = select.select(read_lst,[],[])
    for i in r_lst:
        if i is sk:
            conn,addr = i.accept()
            read_lst.append(conn)
        else:
            msg = i.recv(1024).decode('utf-8')
            print(msg)
            i.send(b'Server Info')
            i.close()
            read_lst.remove(i)
