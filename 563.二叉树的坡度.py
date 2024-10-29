#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def method1():
            ans = 0
            def dfs(node):
                nonlocal ans
                if not node:
                    return 0
                left = dfs(node.left)
                right = dfs(node.right)
                ans += abs(left-right)
                # print(node.val, left, right, ans)
                return left+right+node.val
            dfs(root)
            return ans


        return method1()
# @lc code=end

