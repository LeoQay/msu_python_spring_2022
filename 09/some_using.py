from lru_log import LRUCache


cache = LRUCache(10)
for i in range(12):
    cache[i + 1] = i + 10

cache[3] = 12

v = cache[1000]
