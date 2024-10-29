#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def method1():
            n=len(coins)
            dp=[[float('inf')]*(n+1) for _ in range(amount+1)]
            for i in range(n+1):
                dp[0][i] = 0
            for i in range(1, amount+1):
                for j in range(1, n+1):
                    dp[i][j] = min(dp[i][j], dp[i][j-1])
                    if i-coins[j-1]>=0:
                        dp[i][j]=min(dp[i][j], dp[i-coins[j-1]][j] + 1)
            return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
        def method2():
            n=len(coins)
            dp=[amount+1]*(amount+1)
            dp[0]=0
            for i in range(1, amount+1):
                for c in coins:
                    if i-c>=0:
                        dp[i]=min(dp[i], dp[i-c]+1)
            return dp[-1] if dp[-1] != amount+1 else - 1
        return method2()
        
# @lc code=end

