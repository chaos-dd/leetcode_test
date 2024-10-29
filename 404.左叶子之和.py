#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        is_leaf = lambda n: not n.left and not n.right

        from collections import deque
        dq = deque([root])
        ans = 0
        while len(dq) != 0:
            n = dq.popleft()
            if n.left and is_leaf(n.left):
                ans += n.left.val
            elif n.left:
                dq.append(n.left)
            if n.right:
                dq.append(n.right)
        return ans

# @lc code=end

