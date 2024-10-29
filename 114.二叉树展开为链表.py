#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def method0():
            ls = []
            def dfs(node):
                if not node:
                    return
                ls.append(node)
                dfs(node.left)
                dfs(node.right)
            dfs(root)
            for i in range(1, len(ls)):
                ls[i-1].left=None
                ls[i-1].right=ls[i]

        def method1():
            #先序遍历
            last = None
            def dfs(node):
                nonlocal last
                if not node:
                    return None
                if last:
                    last.right = node
                    last.left = None
                right = node.right
                last = node
                dfs(node.left)
                dfs(right)
            dfs(root)
        def method2():
            #后续遍历
            last = None
            def dfs(node):
                if not node:
                    return
                nonlocal last
                dfs(node.right)
                dfs(node.left)
                node.right = last
                node.left=None
                last=node
            dfs(root)
        def method3():
            node = root
            while node:
                if not node.left:
                    node=node.right
                else:
                    right_most = node.left
                    while right_most.right:
                        right_most = right_most.right
                    right_most.right=node.right
                    node.right=node.left
                    node.left=None
                    node=node.right

        def method4():
            node = root
            while node:
                right_most = node.left
                while right_most and right_most.right:
                    right_most = right_most.right
                right_most.right = node.right
                node.right = node.left
                node.left=node
                node=node.right
           
        return method4()


        
# @lc code=end

