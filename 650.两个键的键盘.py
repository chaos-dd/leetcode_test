#
# @lc app=leetcode.cn id=650 lang=python3
#
# [650] 两个键的键盘
#

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        def method1():
            dp = [[float('inf')]*(n+1) for _ in range(n+1)]
            dp[1][0] = 0
            dp[1][1] = 1
            for i in range(2, n+1):
                #j<i才有意义
                for j in range(1, i):
                    dp[i][j] = dp[i-j][j] + 1
                #i==j只为了算更大的i使用
                dp[i][i] = min(dp[i]) + 1
            # print(dp)
            return min(dp[n])
            pass
        def method2():
            mem = {}
            def dfs(cur, paste):
                if cur == n:
                    return 0
                if cur > n:
                    return float('inf')
                if (cur, paste) in mem:
                    return mem[(cur,paste)]
                n1 = float('inf') if cur == paste else dfs(cur, cur)
                n2 = float('inf') if paste == 0 else dfs(cur+paste, paste)
                res = min(n1,n2) + 1
                mem[(cur,paste)] = res
                return res
            return dfs(1, 0)
        return method1()

# @lc code=end

