#
# @lc app=leetcode.cn id=237 lang=python3
#
# [237] 删除链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        def method1():
            while node.next.next:
                node.val = node.next.val
                node = node.next
            node.val = node.next.val
            node.next = None
        def method2():
            node.val = node.next.val
            node.next = node.next.next
        method2()
        
# @lc code=end

