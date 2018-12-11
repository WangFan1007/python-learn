from multiprocessing import Manager,Process,Lock

def main(dic,lock):
    lock.acquire()
    dic['count'] -= 1
    lock.release()

if __name__ == '__main__':

    m = Manager()

    dic = m.dict({'count':100})

    p_list = []
    lock = Lock()
    for i in range(20):
        p = Process(target=main,args=(dic,lock))
        p.start()
        p_list.append(p)

    [p.join() for p in p_list]

    print(dic['count'])