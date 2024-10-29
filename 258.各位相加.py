#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10 != 0:
            x = num
            num = 0
            while x > 0:
                num += x % 10
                x //= 10
        return num

# @lc code=end

