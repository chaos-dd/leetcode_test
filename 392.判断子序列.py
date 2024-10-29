#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def method1():
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return i == len(s)

        def method2():
            m, n = len(s), len(t)
            dp = [[False]*(n+1) for _ in range(m+1)]
            dp[0][0] = True
            for i in range(n+1):
                dp[0][i] = True
            for i in range(1, m+1):
                for j in range(1, n+1):
                    dp[i][j] = dp[i-1][j-1] if s[i-1] == t[j-1] else dp[i][j-1]
            return dp[m][n]
        return method2()
# @lc code=end

