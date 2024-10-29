#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        def method1():
            n = len(s)
            dp = [0]*(n+1)
            dp[0] =1 
            for i in range(1, n+1):
                if s[i-1] != '0':
                    dp[i] += dp[i-1]
                if i - 2 >= 0 and s[i-2] != '0' and int(s[i-2:i]) <= 26:
                    dp[i] += dp[i-2]
            return dp[n]
        def method2():
            n = len(s)
            dp1 = 1
            dp2 = 0
            
            for i in range(1, n+1):
                dp3 = 0
                if s[i-1] != '0':
                    dp3 = dp1
                if i - 2>= 0 and s[i-2] != '0' and int(s[i-2:i]) <= 26:
                    dp3 += dp2
                dp2 = dp1
                dp1 = dp3
            return dp3
        return method2()

    
# @lc code=end

