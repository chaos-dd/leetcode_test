#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0, 0
            lres = dfs(node.left)
            rres = dfs(node.right)
            return node.val + lres[1] + rres[1], max(lres)+max(rres)
        return max(dfs(root))
        
# @lc code=end

