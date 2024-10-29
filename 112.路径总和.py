#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def method1():
            def target_sum(node, sum):
                if not node:
                    return False
                sum -= node.val
                if sum == 0 and not node.left and not node.right:
                    return True
                if node.left and target_sum(node.left, sum):
                    return True
                if node.right and target_sum(node.right, sum):
                    return True
                return False
            return target_sum(root, targetSum)

        def method2():
            def target(node, sum):
                if not node:
                    return False
                if not node.left and not node.right:
                    return sum == node.val
                return target(node.left, sum - node.val) or \
                target(node.right, sum - node.val)
            return target(root, targetSum)
        def method3():
            if not root:
                return False
            st = [(root, targetSum)]
            while len(st) != 0:
                node, sum = st.pop()
                if not node.left and not node.right and sum == node.val:
                    return True
                if node.left:
                    st.append((node.left, sum-node.val))
                if node.right:
                    st.append((node.right, sum-node.val))
            return False

        return method3()

# @lc code=end

