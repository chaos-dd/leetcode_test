#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def dfs(n):
            nonlocal ans
            if not n:
                return 0
            left = max(0, dfs(n.left))
            right = max(0, dfs(n.right))
            ans = max(ans, left + right + n.val)
            return max(left, right) + n.val
        dfs(root)
        return ans
        
# @lc code=end

