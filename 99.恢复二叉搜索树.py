#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def method1():
            nodes = []
            def inorder(node):
                if not node:
                    return
                inorder(node.left)
                nodes.append(node)
                inorder(node.right)
            inorder(root)
            n1, n2 = None, None
            pre = nodes[0]
            for i in range(1, len(nodes)):
                if pre.val > nodes[i].val:
                    n2 = nodes[i]
                    if not n1:
                        n1 = pre

                pre = nodes[i]
            n1.val, n2.val = n2.val, n1.val
        def method2():

            nodes = [None, None]
            pre = [None]
            def dfs(node):
                if not node:
                    return
                dfs(node.left)
                if pre[0] and pre[0].val > node.val:
                    if not nodes[0]:
                        nodes[0] = pre[0]
                    nodes[1] = node
                pre[0] = node
                dfs(node.right)
            dfs(root)
            nodes[0].val, nodes[1].val = nodes[1].val, nodes[0].val
        return method2()

# @lc code=end

