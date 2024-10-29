#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def method1():
            ans = []
            def dfs(n):
                if not n:
                    return
                dfs(n.left)
                ans.append(n.val)
                dfs(n.right)
            dfs(root)
            return ans
        def method2():
            st = [(root, 0)]
            ans = []
            while st:
                n, flag = st.pop()
                if not n:
                    continue
                if flag == 1:
                    ans.append(n.val)
                else:
                    st.append((n.right, 0))
                    st.append((n, 1))
                    st.append((n.left, 0))
            return ans
        def method3():
            st = []
            node = root
            ans = []
            while st or node:
                while node:
                    st.append(node)
                    node=node.left
                node = st.pop()
                ans.append(node.val)
                node=node.right
            return ans

        return method3()
# @lc code=end

