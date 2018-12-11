from multiprocessing import Queue,Process

def produce(q):
    q.put('Hello')

def consume(q):
    msg = q.get()
    print(msg)

if __name__ == '__main__':
    q = Queue()

    p = Process(target=produce,args=(q,))
    p.start()

    c = Process(target=consume,args=(q,))
    c.start()



