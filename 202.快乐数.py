#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def method1():
            dup = set()
            while n != 1:
                x = 0
                while n != 0:
                    x += (n % 10) ** 2
                    n //= 10
                n = x
                if n in dup:
                    return False
                dup.add(n)
            return True
        def method2():
            def get_next(x):
                y = 0
                while x != 0:
                    y += (x %10)**2
                    x //= 10
                return y
            slow, fast = n, get_next(n)
            while slow != fast and fast != 1:
                slow = get_next(slow)
                fast = get_next(get_next(fast))
            return fast == 1
        return method2()
# @lc code=end

