#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(math.pow(c, 0.5))
        while l <= r:
            s = l ** 2 + r **2
            if s == c:
                return True
            elif s < c:
                l += 1
            else:
                r -= 1
        return False
# @lc code=end

