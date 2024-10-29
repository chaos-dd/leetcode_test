#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def method1():
            dummy = ListNode()
            dummy.next = head
            node = dummy
            while node and node.next and node.next.next:
                next = node.next
                next2 = next.next
                next3 = next2.next
                node.next = next2
                next2.next = next
                next.next = next3
                node=next
            return dummy.next
        def method2():
            if not head or not head.next:
                return head
            new_head = head.next
            head.next = self.swapPairs(new_head.next)
            new_head.next = head
            return new_head
        return method2()

        
# @lc code=end

