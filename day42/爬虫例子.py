from gevent import monkey;monkey.patch_all()

import requests
import gevent

url = 'http://www.baidu.com'

def get_url(url):
    resp = requests.get(url)
    content = resp.content.decode('utf-8')
    # print(content)
    return len(content)


g1 = gevent.spawn(get_url,'http://www.baidu.com')
g2 = gevent.spawn(get_url,'http://www.souhu.com')
g3 = gevent.spawn(get_url,'http://www.hao123.com')
g4 = gevent.spawn(get_url,'http://www.taobao.com')

gevent.joinall([g1,g2,g3,g4])

print(g1.value)
print(g2.value)
print(g3.value)
print(g4.value)