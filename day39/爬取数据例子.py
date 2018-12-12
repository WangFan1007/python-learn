import requests
from multiprocessing import Pool

def get(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return url,resp.content

def call_back(args):
    url,content = args
    print(url,len(content))


url_list = ['http://www.baidu.com',
            'http://www.sohu.com',
            'http://www.sina.com']

if  __name__ == '__main__':
    p = Pool()

    for url in url_list:
        p.apply_async(get,args=(url,),callback=call_back)
    p.close()
    p.join()



