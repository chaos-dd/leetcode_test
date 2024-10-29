#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same(node1, node2):
            if node1 and node2 and node1.val == node2.val:
                return is_same(node1.left, node2.left) and is_same(node1.right, node2.right)
            if not node1 and not node2:
                return True
            return False
        def dfs(node1, node2):
            if is_same(node1, node2):
                return True
            if node1.left and dfs(node1.left, node2):
                return True
            if node1.right and dfs(node1.right, node2):
                return True
            return False
        return dfs(root, subRoot)

# @lc code=end

