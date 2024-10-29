#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        prefix = 0
        def dfs(node):
            nonlocal prefix
            if not node:
                return
            dfs(node.right)
            prefix += node.val
            node.val = prefix
            dfs(node.left)
        dfs(root)
        return root
        
# @lc code=end

