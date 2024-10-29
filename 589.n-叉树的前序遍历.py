#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def method1():
            ans = []
            def dfs(node):
                if not node:
                    return
                ans.append(node.val)
                for n in node.children:
                    dfs(n)
            dfs(root)
            return ans
        
        def method2():
            ans = []
            st = [root]
            while len(st) != 0:
                node = st.pop()
                if not node:
                    continue
                ans.append(node.val)
                for n in reversed(node.children):
                    st.append(n)
            return ans
        return method2()
        
# @lc code=end

