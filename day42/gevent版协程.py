from gevent import monkey;monkey.patch_all()
import time
import gevent

def eat():
    print('eating start')
    time.sleep(1)
    # gevent.sleep(1)
    print('eating end')



def play():
    print('playing start')
    time.sleep(1)
    # gevent.sleep(1)
    print('playing end')

g1 = gevent.spawn(eat)
g2 = gevent.spawn(play)

g1.join()
g2.join()