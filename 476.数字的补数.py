#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        high = 32
        for i in range(31, -1, -1):
            if num &(1<<i) != 0:
                high = i
                break
        # print(high)
        mask = (1<<(high+1)) -1
        # print(bin(mask))
        return num ^ mask
# @lc code=end

