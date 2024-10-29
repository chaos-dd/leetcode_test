#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        while x != 0:
            num = x %10
            if x < 0 and num > 0:
                num -= 10
            if (2**31-1-num)/10 < res or \
                (-2**31-num)/10 > res:
                return 0
            res = res*10 + num
            if x > 0:
                x //=10
            else:
                x = (x-num)//10
        return res

        
# @lc code=end

