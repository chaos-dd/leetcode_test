#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node):
            if not node:
                return 0
            dl = depth(node.left)
            dr = depth(node.right)
            return -1 if dl == -1 or dr == -1 or abs(dl-dr)>1 else max(dl, dr) + 1
        return depth(root) != -1
        
# @lc code=end

