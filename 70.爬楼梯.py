#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        def method1():
            n2, n1 = 0, 1
            for i in range(1, n + 1):
                n0 = n2+n1
                n2, n1=n1,n0
            return n1
        def method2():
            m = 2
            dp = [0]*(n+1)
            dp[0] = 1
            for i in range(1, n+1):
                for j in range(1, m + 1):
                    if i - j>=0:
                        dp[i] += dp[i-j]
            return dp[-1]

        return method2()
# @lc code=end

