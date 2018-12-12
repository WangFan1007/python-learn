
import time
from threading import Lock,Thread


noddle_lock = Lock()
fork_lock = Lock()

def eat1(name):
    noddle_lock.acquire()
    print('%s拿到面了'%name)
    fork_lock.acquire()
    print('%s拿到叉子了'%name)
    print('%s吃面'%name)
    time.sleep(0.2)
    fork_lock.release()
    noddle_lock.release()

def eat2(name):

    fork_lock.acquire()
    print('%s拿到叉子了'%name)
    noddle_lock.acquire()
    print('%s拿到面了' % name)
    print('%s吃面'%name)
    time.sleep(0.2)
    noddle_lock.release()
    fork_lock.release()


Thread(target=eat1,args=('jason',)).start()
Thread(target=eat2,args=('rune',)).start()
Thread(target=eat1,args=('foay',)).start()
Thread(target=eat2,args=('roya',)).start()