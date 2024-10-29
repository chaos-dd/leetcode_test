#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def method1():
            pre = None
            def dfs(node):
                nonlocal pre
                if not node:
                    return True
                if not dfs(node.left):
                    return False
                if pre and node.val <= pre.val:
                    return False
                pre = node
                return dfs(node.right)
            return dfs(root)
        def method2():
            def dfs(node, lower, upper):
                if not node:
                    return True
                if not dfs(node.left, lower, node.val):
                    return False
                if node.val <= lower or node.val >= upper:
                    return False
                return dfs(node.right, node.val, upper)
            return dfs(root, float('-inf'), float('inf'))
        def method3():
            def dfs(node):
                if not node:
                    return True, float('inf'), float('-inf')
                res_left = dfs(node.left)
                if not res_left[0] or node.val <= res_left[2]:
                    return False, None, None
                res_right = dfs(node.right)
                if not res_right[0] or node.val >= res_right[1]:
                    return False, None, None
                return True, min(node.val, res_left[1]), max(node.val, res_right[2])
            return dfs(root)[0]

        return method3()



# @lc code=end

