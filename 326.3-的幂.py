#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3 的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 :
            return False

        def method1():
            nonlocal n
            while n != 0 and n > 1:
                n /= 3
                # print(n)
            return n == 1
        def method2():
            x = 1
            while x < n:
                x *= 3
            return x == n
        def method3():
            nonlocal n
            while n > 0 and n % 3 == 0:
                n /= 3
            return n == 1
        def method4():
            nonlocal n
            while n % 3 == 0:
                n /= 3
            return n == 1

        return method4()
# @lc code=end

