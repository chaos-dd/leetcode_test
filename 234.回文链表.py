#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def dfs(node):
            nonlocal head
            if not node:
                return True
            if not dfs(node.next):
                return False
            if node.val != head.val:
                return False
            head=head.next
            return True
        return dfs(head)

        
# @lc code=end

