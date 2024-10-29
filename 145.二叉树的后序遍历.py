#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def method1():
            def dfs(node):
                if not node:
                    return
                dfs(node.left)
                dfs(node.right)
                ans.append(node.val)
            ans = []
            dfs(root)
            return ans
        def method2():
            st = [(root, 0)]
            ans = []
            while len(st) != 0:
                node, tp = st.pop()
                if not node:
                    continue
                if tp == 0:
                    st.append((node, 1))
                    st.append((node.right, 0))
                    st.append((node.left, 0))
                else:
                    ans.append(node.val)
            return ans
        
        return method2()
# @lc code=end

