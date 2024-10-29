#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def method1():
            nums = [1] + nums + [1]
            n = len(nums)
            dp = [[0]*n for _ in range(n)]
            for i in range(n-2, -1, -1):
                for j in range(i+1, n):
                    for k in range(i+1, j):
                        dp[i][j] = max(dp[i][j], 
                            dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j]
                            )
            return dp[0][-1]
        def method2():
            from functools import cache
            nonlocal nums
            nums = [1]+nums+[1]
            @cache
            def dfs(l, r):
                if l >= r:
                    return 0
                res = 0
                for i in range(l+1, r):
                    res = max(res, dfs(l, i) + dfs(i, r) + nums[l]*nums[i]*nums[r])
                return res
            return dfs(0, len(nums)-1)
        return method2()
        
# @lc code=end

