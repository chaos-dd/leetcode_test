#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if node.val == status[0]:
                status[1] += 1
            else:
                status[0] = node.val
                status[1] = 1
            if status[1] == status[2]:
                status[3].append(node.val)
            elif status[1] > status[2]:
                status[2] = status[1]
                status[3] = [node.val]

            dfs(node.right)
        #pre, cnt, max_cnt, ans
        status = [0, 0, 0, []]
        dfs(root)
        return status[3]
# @lc code=end

