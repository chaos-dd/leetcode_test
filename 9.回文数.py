#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = 0
        z=x
        while x != 0:
            y = y * 10 + x%10
            x//=10
        return z == y

        
# @lc code=end

