#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        def method1():
            ans = [0]*(n+1)
            for i in range(n+1):
                cnt = 0
                x = i
                while x > 0:
                    cnt += (x&1)
                    x >>=1
                ans[i]=cnt
            return ans
        def method2():
            ans = [0]*(n+1)
            for i in range(1, n+1):
                ans[i] = ans[i&(i-1)] + 1
            return ans
        return method2()
        
# @lc code=end

