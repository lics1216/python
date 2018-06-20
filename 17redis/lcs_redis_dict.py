from redis import Redis

import json

class RedisDict:
    def __init__(self, prefix=''):
        self.data = Redis()
        self.prefix = prefix

    def get(self, key):
        redis_key = self.prefix + '_' + key
        redis_val = self.data.get(redis_key)
        if redis_val is None:
            return None
        else:
            return json.loads(redis_val)

    def set(self, key, val):
        redis_key = self.prefix + '_' + key
        redis_val = json.dumps(val)
        self.data.set(redis_key, redis_val)

    def pop(self, key):
        redis_key = self.prefix + '_' + key
        self.data.delete(redis_key)

    def __iter__(self):
        for item in self.data.keys(self.prefix + '*'):
            prefix, key = decode(item)
            yield key


def decode(redis_key):
    sep = redis_key.find('_')
    prefix = redis_key[:sep]
    key = redis_key[sep+1:]
    return prefix, key

if __name__ == '__main__':
    r = RedisDict('online')
    r.set('user', [1,[{'name':'yichya'}]])
    for item in r:
        print(item)
        print(r.get(item))