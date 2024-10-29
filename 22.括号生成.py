#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        cur = []
        def dfs(left, right):
            if left == right and left == n:
                ans.append(''.join(cur))
                return
            if left<n:
                cur.append('(')
                dfs(left+1, right)
                cur.pop()
            if right<left:
                cur.append(')')
                dfs(left, right+1)
                cur.pop()
        dfs(0, 0)
        return ans

# @lc code=end

