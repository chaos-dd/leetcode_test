#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        def method1():
            last = 2
            while n > 0:
                cur = n % 2
                if cur == last:
                    return False
                last = cur
                n >>= 1
            return True
        def method2():
            a = n^ (n>>1) #全1
            return a & (a+1) == 0
        return method2()


# @lc code=end

