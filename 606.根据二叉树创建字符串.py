#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(node):
            if not node:
                return ''
            res = f'{node.val}'
            left = dfs(node.left)
            right = dfs(node.right)
            if len(left) != 0 or len(right) != 0:
                res += f'({left})'
            if len(right) != 0:
                res += f'({right})'
            return res
        return dfs(root)

# @lc code=end

