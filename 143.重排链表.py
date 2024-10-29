#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def method1():
            st = []
            node = head.next
            while node:
                st.append(node)
                node = node.next
            node = head
            i, j = 0, len(st)-1
            while i < j:
                # print(st[i].val, st[j].val)
                node.next = st[j]
                node = node.next
                node.next = st[i]
                node = node.next
                i += 1
                j -= 1
            # print(node)
            if i == j:
                node.next = st[i]
                node = node.next
            node.next = None
        def method2():
            fast, slow = head, head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None

            pre = None
            node = mid
            while node:
                next = node.next
                node.next = pre
                pre = node
                node = next
            node1, node2 = head, pre
            while node1 and node2:
                next1, next2 = node1.next, node2.next
                node1.next = node2
                node2.next = next1
                node1, node2 = next1, next2

        return method2()

# @lc code=end

