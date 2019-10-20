
import redis  

# r = redis.StrictRedis(host='127.0.0.1', port=6379)
# di = {}
# di['banana'] = 2
# di['pear']  = '的解放路口'
# r.hmset('price', di)
# # 现在 banana 和 pear 存在内存中，就是在 本台电脑另外一个编译器，或者jupyter nobebook ，
# # 调用  rgetall('price') ， 也能得到数据
# keys = r.keys()
# for x in keys:
#     #print(x.decode("utf-8"))
#     print(x)
# print('第五人格'.encode('utf-8'))
# data = r.hgetall('第五人格'.encode('utf-8'))
# for x,y in data.items():
#     print("%s:%s" %(x.decode('utf-8'),y.decode('utf-8')))

x = ['s','1','1','2','2']
import random
print( random.randint(1,20))
