#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def find(root, node, path):
            if not root:
                return False
            path.append(root)
            if root.val == node.val:
                return True
            if node.val < root.val and find(root.left, node, path):
                return True
            if node.val > root.val and find(root.right, node, path):
                return True
            path.pop()
            return False
        path1, path2 = [], []
        find(root, p, path1)
        find(root, q, path2)
        i = 0
        ans = None
        while i < len(path1) and i < len(path2):
            if path1[i].val == path2[i].val:
                ans = path1[i]
            i += 1
        # print(len(path1), len(path2), i)
        return ans
        

        
# @lc code=end

