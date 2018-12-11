from multiprocessing import Pipe,Process


def func(conn1,conn2):
    conn2.close()
    while True:
        try:
            msg = conn1.recv()
            print(msg)
        except EOFError:
            conn1.close()
            break



if __name__ == '__main__':
    conn1, conn2 = Pipe()

    Process(target=func,args=(conn1,conn2)).start()
    for i in range(20):
        conn2.send("吃了吗")

    conn1.close()
    conn2.close()