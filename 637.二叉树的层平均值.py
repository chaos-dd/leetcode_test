#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def method1():
            from collections import deque
            dq = deque([root])
            ans = []
            while len(dq) != 0:
                ln = len(dq)
                s = 0
                for i in range(ln):
                    node = dq.popleft()
                    s += node.val
                    if node.left:
                        dq.append(node.left)
                    if node.right:
                        dq.append(node.right)
                ans.append(s*1.0/ln)
            return ans
        def method2():
            count = []
            sum = []
            def helper(node, level):
                if not node:
                    return
                if level >= len(count):
                    count.append(0)
                    sum.append(0)
                count[level] += 1
                sum[level] += node.val
                helper(node.left, level+1)
                helper(node.right, level+1)
            helper(root, 0)
            for idx in range(len(count)):
                sum[idx] /= float(count[idx])

            return sum

        return method2()

            

# @lc code=end

