import socket

sk = socket.socket()
sk.connect(('127.0.0.1',8080))


msg = input('>>>')
sk.send(msg.encode('utf-8'))

info = sk.recv(1024).decode('utf-8')
print(info)
sk.close()