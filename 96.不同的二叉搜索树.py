#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        def method1():
            from functools import cache
            @cache
            def dfs(n):
                if n <= 1:
                    return 1
                res = 0
                for i in range(n):
                    res += dfs(i) *dfs(n-i-1)
                return res
            return dfs(n)
        def method2():
            from functools import cache
            @cache
            def dfs(l, r):
                if l>=r:
                    return 1
                res = 0
                for i in range(l, r+1):
                    res += dfs(l,i-1) *dfs(i+1, r)
                return res
            return dfs(1, n)

        def method3():
            dp = [0]*(n+1)
            dp[0]=dp[1]=1
            for i in range(2, n+1):
                for j in range(1, i+1):
                    dp[i] += dp[j-1]*dp[i-j]
            return dp[-1]

        return method3()

# @lc code=end

