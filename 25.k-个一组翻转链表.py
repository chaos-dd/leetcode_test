#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def rev(node):
            prev = None
            while node:
                next = node.next
                node.next=prev
                prev = node
                node=next
        dummy = ListNode()
        prev_end = dummy
        start, end = head, head
        while end:
            for i in range(k-1):
                if end:
                    end = end.next
            if not end:
                prev_end.next = start
                break
            next_start = end.next
            end.next = None
            rev(start)
            prev_end.next = end
            prev_end = start
            start = next_start
            end = start
        return dummy.next


        
# @lc code=end

