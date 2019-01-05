import redis

#基本使用
# conn = redis.Redis(host='192.168.195.128',port=6379,password='wangfan')
# conn.set('x1','wangfan',ex=5)
# temp = conn.get('x1')
# print(temp)

#使用连接池
pool = redis.ConnectionPool(host='192.168.195.128',port=6379,password='wangfan',max_connections=1000)
conn = redis.Redis(connection_pool=pool)

conn.set('foo','bar')

resul = conn.get('foo')
print(resul)