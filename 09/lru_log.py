import sys
from dataclasses import dataclass
from typing import Any
import logging


file_log = logging.FileHandler('cache.log', 'w')
logging.basicConfig(
    handlers=(file_log,),
    level=logging.DEBUG,
    format='%(asctime)s\t%(levelname)s\t%(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class Pair:
    key: Any
    value: Any

    def __str__(self):
        return f'[key: {self.key}, value: {self.value}]'


@dataclass
class Node:
    left: 'Node' = None
    right: 'Node' = None
    pair: Any = None


class MyList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push_back(self, node):
        self.size += 1
        if self.first is None:
            self.first = node
            self.last = node
            return
        last = self.last
        last.right = node
        self.last = node
        node.left = last
        node.right = None

    def pop_front(self):
        if self.first is None:
            raise KeyError
        if self.first is self.last:
            first = self.first
            self.first = None
            self.last = None
        else:
            first = self.first
            self.first = first.right
            self.first.left = None
        self.size -= 1
        return first

    def pop_back(self):
        if self.first is None:
            raise KeyError
        if self.first is self.last:
            last = self.last
            self.first = None
            self.last = None
        else:
            last = self.last
            self.last = last.left
            self.last.right = None
        self.size -= 1
        return last

    def erase(self, node):
        if self.first is None:
            raise KeyError
        if self.first is self.last:
            if self.first is not node:
                raise KeyError
            self.first = None
            self.last = None
            self.size -= 1
        elif self.first is node:
            self.pop_front()
        elif self.last is node:
            self.pop_back()
        else:
            node.right.left = node.left
            node.left.right = node.right
            self.size -= 1

    def __len__(self):
        return self.size


class LRUCache:
    def __init__(self, size=50):
        logger.info('LRUCache: __init__ with size %s', size)
        self.size = size
        self.queue = MyList()
        self.arr = {}

    def __getitem__(self, key):
        logger.info('LRUCache: called with key %s', key)
        if key not in self.arr:
            logger.warning('LRUCache: in __getitem__ key %s does not exist', key)
            return None
        node = self.arr[key]
        self.update_used(node)
        logger.info('LRUCache: __getitem__: return: %s', node.pair)
        return node.pair.value

    def __setitem__(self, key, value):
        pair = Pair(key, value)
        logger.info('LRUCache: __setitem__: %s', pair)
        if key in self.arr:
            node = self.arr[key]
            node.pair.value = value
            self.update_used(node)
            logger.info('LRUCache: __setitem__: set: %s', pair)
            return
        self.pop()
        node = Node(pair=Pair(key, value))
        self.queue.push_back(node)
        self.arr[key] = node
        logger.info('LRUCache: __setitem__: set: %s', pair)

    def pop(self):
        if len(self.queue) < self.size:
            return
        deleted = self.queue.pop_front().pair
        logger.info('LRUCache: pop: %s', deleted)
        del self.arr[deleted.key]

    def update_used(self, node):
        self.queue.erase(node)
        self.queue.push_back(node)
        logger.info('LRUCache: updated: %s', node.pair)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-s':
        stdout_log = logging.StreamHandler()
        form = logging.Formatter('%(message)s')
        stdout_log.setFormatter(form)
        logger.addHandler(stdout_log)

    cache = LRUCache(10)
    for i in range(12):
        cache[i + 1] = i + 10

    cache[3] = 12

    none_smth = cache[1000]
