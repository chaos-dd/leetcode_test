#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast= head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                fast = head
                while slow != fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None
        
# @lc code=end

