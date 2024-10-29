#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        # while n % 2 == 0:
        #     n = n >>1
        #     # print(n)
        # return n == 1
        return n > 0 and n & (n-1) == 0
# @lc code=end

