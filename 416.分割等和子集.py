#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def method1():
            target = sum(nums)
            if target % 2 != 0:
                return False
            target //= 2
            n=len(nums)
            dp = [[False]*(n+1) for _ in range(target+1)]
            for i in range(n+1):
                dp[0][i]=True
            for i in range(1, target+1):
                for j in range(1, n+1):
                    dp[i][j] = dp[i][j-1]
                    if i-nums[j-1]>=0:
                        dp[i][j]=dp[i][j] or dp[i-nums[j-1]][j-1]
            return dp[-1][-1]
        def method2():
            from functools import cache
            target = sum(nums)
            if target % 2 != 0:
                return False
            target //= 2
            @cache
            def check(idx, target):
                if target<0:
                    return False
                if target == 0:
                    return True
                if idx>=len(nums):
                    return False
                return check(idx+1, target) or check(idx+1, target-nums[idx])
            return check(0, target)
        return method2()


        
# @lc code=end

