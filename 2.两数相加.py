#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        ex = 0
        while l1 or l2 or ex:
            val = ex
            if l1:
                val += l1.val
                l1=l1.next
            if l2:
                val += l2.val
                l2=l2.next
            ex = val // 10
            val = val % 10
            node.next = ListNode(val)
            node=node.next
        return dummy.next

# @lc code=end

