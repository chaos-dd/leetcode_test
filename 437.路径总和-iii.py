#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def method1():
            ans = 0
            def root_sum(node, target):
                nonlocal ans
                if not node:
                    return
                target -= node.val
                if target == 0:
                    ans += 1
                root_sum(node.left, target)
                root_sum(node.right, target)
            def path_sum(node, target):
                root_sum(node, target)
                if node:
                    path_sum(node.left, target)
                    path_sum(node.right, target)
                return
            path_sum(root, targetSum)
            return ans
        def method2():
            from collections import defaultdict
            prefix = defaultdict(int)
            prefix[0]=1
            ans = 0
            def dfs(node, cur):
                nonlocal ans
                if not node:
                    return
                cur += node.val
                ans += prefix[cur-targetSum]
                prefix[cur]+=1
                dfs(node.left, cur)
                dfs(node.right, cur)
                prefix[cur]-=1
            dfs(root, 0)
            return ans

        return method2()
        
# @lc code=end

