import redis  


# Redis是封装了Redis数据库操作的类,并提供了类似的API.
# 一个redis实例只维护一个数据表而应用中经常出现需要维护多个字典的情况.

  
r = redis.StrictRedis(host='127.0.0.1', port=6379)  
r.set('foo', 'hello')  
r.rpush('mylist', '李长松')  

print(r.get("foo"))

print(r.rpop('mylist'))  # 为什么输出的是二进制的

# ###############
# 使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)  
r = redis.Redis(connection_pool=pool)  
r.set('one', 'first')  
r.set('two', 'second')  
print (r.get('one') ) 
print (r.get('two') )


# ##############
# redis pipeline机制，可以在一次请求中执行多个命令，这样避免了多次的往返时延。
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)    
r = redis.Redis(connection_pool=pool)    
pipe = r.pipeline()    
pipe.set('one', 'first')    
pipe.set('two', 'second')    
pipe.execute()    
    
pipe.set('one'. 'first').rpush('list', 'hello').rpush('list', 'world').execute() 