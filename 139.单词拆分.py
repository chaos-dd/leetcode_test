#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def method1():
            mem = set(wordDict)
            n=len(s)
            dp=[False]*(n+1)
            dp[0]=True
            for i in range(1, n+1):
                for j in range(1, i+1):
                    if s[i-j:i] in mem and dp[i-j]:
                        dp[i] = True
                        break
            return dp[-1]
        def method2():
            mem = set(wordDict)
            n=len(s)
            dp=[False]*(n+1)
            dp[0]=True
            for i in range(1, n+1):
                for j in range(i):
                    if dp[j] and s[j:i] in mem:
                        dp[i]=True
                        break

            return dp[-1]

        return method2()

        
# @lc code=end

