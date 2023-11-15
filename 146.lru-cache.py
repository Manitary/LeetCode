#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
# from typing import Self


class Node:
    def __init__(self, key: int = 0, value: int = 0) -> None:
        self.key = key
        self.value = value
        # self.left: Self | None = None
        # self.right: Self | None = None
        self.left = None
        self.right = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: dict[int, Node] = {}
        self.lru = Node()
        self.mru = Node()
        self.lru.right, self.mru.left = self.mru, self.lru

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_mru(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_mru(node)
            return
        node = Node(key, value)
        self.append_node(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            to_remove = self.lru.right
            self.remove_node(to_remove)
            del self.cache[to_remove.key]

    def remove_node(self, node: Node) -> None:
        node.left.right, node.right.left = node.right, node.left

    def append_node(self, node: Node) -> None:
        left, right = self.mru.left, self.mru
        left.right = self.mru.left = node
        node.left, node.right = left, right

    def move_to_mru(self, node: Node) -> None:
        self.remove_node(node)
        self.append_node(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# @lc code=end
