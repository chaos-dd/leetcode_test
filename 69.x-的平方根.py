#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l <= r:
            m = l + (r - l) // 2
            s = m * m
            if s == x:
                return m
            elif s < x:
                l = m + 1
                res = m
            else:
                r = m -1
        return res
        
# @lc code=end

