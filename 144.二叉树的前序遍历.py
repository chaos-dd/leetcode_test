#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def method1():
            res = []
            def dfs(node):
                if not node:
                    return
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)
            dfs(root)
            return res
        def method2():
            res = []
            st = []
            if root:
                st.append(root)
            while len(st):
                node = st.pop()
                res.append(node.val)
                if node.right:
                    st.append(node.right)
                if node.left:
                    st.append(node.left)
            return res

        return method2()

# @lc code=end

