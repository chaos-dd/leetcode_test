#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
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
    def postorder(self, root: 'Node') -> List[int]:
        def method1():
            ans = []
            def dfs(node):
                if not node:
                    return
                for n in node.children:
                    dfs(n)
                ans.append(node.val)
            dfs(root)
            return ans
        def method2():
            ans = []
            st = [(root, 0)]
            while len(st) != 0:
                node, tp = st.pop()
                if not node:
                    continue
                if tp == 1:
                    ans.append(node.val)
                else:
                    st.append((node, 1))
                    st.extend([(v, 0) for v in reversed(node.children)])
            return ans
        return method2()
        
# @lc code=end

