#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def method1():
            def dfs(n1, n2):
                if not n1 and not n2:
                    return True
                if not n1 or not n2:
                    return False
                if n1.val != n2.val:
                    return False
                return dfs(n1.left, n2.right) and dfs(n1.right, n2.left)
            return not root or dfs(root.left, root.right)
        def method2():
            if not root:
                return True
            st = [root.left, root.right]
            while st:
                n1 = st.pop()
                n2 = st.pop()
                if not n1 and not n2:
                    continue
                if not n1 or not n2:
                    return False
                if n1.val != n2.val:
                    return False
                st.append(n1.left)
                st.append(n2.right)
                st.append(n1.right)
                st.append(n2.left)
            return True

        return method2()

# @lc code=end

