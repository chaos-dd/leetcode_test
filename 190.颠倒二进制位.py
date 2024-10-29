#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        cnt = 0
        while cnt < 32:
            # print(bin(n), bin(ans))
            ans <<= 1
            ans |= (n&1)
            n >>=1
            cnt += 1
        return ans

        
# @lc code=end

