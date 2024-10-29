#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        nums = [[0,0] for _ in range(len(strs))]

        for i in range(len(strs)):
            for j in range(len(strs[i])):
                if strs[i][j] == '0':
                    nums[i][0] += 1
            nums[i][1] = len(strs[i]) - nums[i][0]
        
        # print(nums)
        dp = [[[0]*(n+1) for _ in range(m+1)] for _ in range(len(strs)+1)]
        for i in range(1, len(strs)+1):
            #需要算dp[*][1][0], dp[*][0][1]，所以m，n需要从0开始
            for j in range(m+1):
                for k in range(n+1):
                    dp[i][j][k] = dp[i-1][j][k]
                    if j-nums[i-1][0] >= 0 and k-nums[i-1][1] >=0:
                        dp[i][j][k] = max(dp[i-1][j-nums[i-1][0]][k-nums[i-1][1]]+1,
                                dp[i][j][k])
        # print(dp)
        return dp[len(strs)][m][n]

# @lc code=end

