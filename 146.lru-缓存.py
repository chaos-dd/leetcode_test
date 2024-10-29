#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class ListNode:
    def __init__(self, key=0, val=0):
        self.key=key
        self.val=val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode()
        self.end = ListNode()
        self.head.next = self.end
        self.end.prev = self.head
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_end(node)
        return node.val
    
    def _move_to_end(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self._append_to_end(node)

    def _append_to_end(self, node):
        node.prev = self.end.prev
        node.next = self.end
        self.end.prev.next = node
        self.end.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_end(node)
        else:
            if len(self.cache) >= self.capacity:
                node = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                self.cache.pop(node.key)
            node=ListNode(key, value)
            self.cache[key]=node
            self._append_to_end(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

