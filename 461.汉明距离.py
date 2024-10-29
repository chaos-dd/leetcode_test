#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def method1():
            nonlocal x, y
            ans = 0
            while x or y:
                ans += 1 if x&1 != y&1 else 0
                x >>= 1
                y >>= 1
            return ans
        def method2():
            diff = x^y
            ans = 0
            while diff>0:
                ans += 1
                diff = diff&(diff-1)
            return ans
        return method2()
        
# @lc code=end

