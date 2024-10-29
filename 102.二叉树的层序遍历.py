#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        dq = deque([root])
        ans = []
        while dq:
            cur = []
            sz = len(dq)
            while sz >0:
                sz -= 1
                n = dq.popleft()
                if not n:
                    continue
                cur.append(n.val)
                dq.append(n.left)
                dq.append(n.right)
            if cur:
                ans.append(cur)
        return ans

# @lc code=end

