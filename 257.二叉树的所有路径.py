#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def path(node, res, cur):
            cur.append(node.val)
            if not node.left and not node.right:
                res.append('->'.join(map(str, cur[:])))
                cur.pop()
                return
            if node.left:
                path(node.left, res, cur)
            if node.right:
                path(node.right, res, cur)
            cur.pop()
        
        res = []
        cur = []
        path(root, res, cur)
        return res

# @lc code=end

