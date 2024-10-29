#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        hp = []
        for node in lists:
            if node:
                heapq.heappush(hp, (node.val, id(node), node))
        dummy = ListNode()
        node = dummy
        while hp:
            _, _, n = hp[0]
            heapq.heappop(hp)
            node.next = n
            node=node.next
            if n.next:
                heapq.heappush(hp, (n.next.val, id(n.next), n.next))
        return dummy.next

# @lc code=end

