#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        target = s-target
        #关键
        if target<0:
            return 0
        if target %2 != 0:
            return 0
        target //= 2
        n=len(nums)
        dp = [[0]*(n+1) for _ in range(target+1)]
        # [1,0] 组成0有两种情况，一种是什么都不选，一种是选第二个
        #所以不能按照下面的初始化，target=0的情况也需要遍历
        #for i in range(n+1):
        #    dp[0][i]=1
        dp[0][0]=1
        for i in range(target+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i][j-1]
                if i-nums[j-1] >= 0:
                    dp[i][j] += dp[i-nums[j-1]][j-1]
        return dp[-1][-1]
        
# @lc code=end

