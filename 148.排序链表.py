#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(n1,n2):
            dummy = ListNode()
            node=dummy
            while n1 and n2:
                if n1.val < n2.val:
                    node.next=n1
                    n1=n1.next
                else:
                    node.next=n2
                    n2=n2.next
                node=node.next
            if n1:
                node.next=n1
            if n2:
                node.next=n2
            return dummy.next
        def sort(node):
            if not node or not node.next:
                return node
            slow, fast=node, node.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            next_head = slow.next
            slow.next = None
            n1=sort(node)
            n2=sort(next_head)
            return merge(n1, n2)
        return sort(head)
        
# @lc code=end

