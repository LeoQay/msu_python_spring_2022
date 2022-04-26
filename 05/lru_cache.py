from dataclasses import dataclass
from typing import Any


@dataclass
class Pair:
    key: Any
    value: Any


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
        self.size = size
        self.queue = MyList()
        self.arr = {}

    def __getitem__(self, key):
        if key not in self.arr:
            return None
        node = self.arr[key]
        self.update_used(node)
        return node.pair.value

    def __setitem__(self, key, value):
        if key in self.arr:
            node = self.arr[key]
            node.pair.value = value
            self.update_used(node)
            return
        self.pop()
        node = Node(pair=Pair(key, value))
        self.queue.push_back(node)
        self.arr[key] = node

    def pop(self):
        if len(self.queue) < self.size:
            return
        deleted = self.queue.pop_front()
        del self.arr[deleted.pair.key]

    def update_used(self, node):
        self.queue.erase(node)
        self.queue.push_back(node)
