#
# @lc app=leetcode.cn id=1110 lang=python3
#
# [1110] 删点成林
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        def del_node(node):
            if not node:
                return
            node.left = del_node(node.left)
            node.right = del_node(node.right)
            if node.val in to_delete:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
                return None
            return node
        res = []
        node = del_node(root)
        if node:
            res.append(node)
        return res
        
# @lc code=end

