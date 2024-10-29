#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def find(res, cur, node, sum):
            if not node:
                return
            cur.append(node.val)
            sum -= node.val
            if node.left is None and node.right is None and sum == 0:
                res.append(cur[:])
            find(res, cur, node.left, sum)
            find(res, cur, node.right, sum)
            cur.pop()
            return
        res = []
        cur = []
        find(res, cur, root, targetSum)
        return res


# @lc code=end

