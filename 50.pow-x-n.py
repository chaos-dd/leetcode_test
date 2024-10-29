#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def method1():
            nonlocal n
            ans = 1
            flag=1
            if n < 0:
                n=-n
                flag = 0
            for i in range(n):
                ans *= x
            return ans if flag == 1 else 1/ans
        def method2():
            def foo(x, n):
                flag = 1
                if n < 0:
                    flag = 0
                    n = -n
                if n == 0:
                    return 1
                res = foo(x, n//2)
                res = res*res
                if n % 2 == 1:
                    res *= x
                return res if flag == 1 else 1/res
            return foo(x,n)
        return method2()
        
# @lc code=end

