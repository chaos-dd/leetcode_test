#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def method1():

            def build(pre_root, in_start, in_end):
                if in_start>in_end:
                    return None
                in_root = inorder.index(preorder[pre_root], in_start, in_end+1)
                node=TreeNode(preorder[pre_root])
                node.left = build(pre_root+1, in_start, in_root-1)
                node.right = build(pre_root+1+in_root-in_start, in_root+1, in_end)
                return node
            return build(0, 0, len(inorder)-1)
        return method1()

# @lc code=end

