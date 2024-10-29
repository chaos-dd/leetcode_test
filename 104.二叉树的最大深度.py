#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def method1():
            def dfs(n):
                if not n:
                    return 0
                res = 1 + max(dfs(n.left), dfs(n.right))
                return res
            return dfs(root)
        def method2():
            if not root:
                return 0
            from collections import deque
            dq = deque([root])
            ans = 0
            while dq:
                ans += 1
                sz = len(dq)
                while sz > 0:
                    sz -= 1
                    n = dq.popleft()
                    if n.left:
                        dq.append(n.left)
                    if n.right:
                        dq.append(n.right)
            return ans
        return method2()

# @lc code=end

