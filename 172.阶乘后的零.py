#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        def method1():
            n1 = 0 
            for i in range(1, n+1):
                while i % 5 == 0:
                    n1 += 1
                    i /= 5
            return n1
        def method2():
            # 统计 5 的个数
            cnt = 0
            div = 5
            while div <= n:
                cnt += n//div
                div *= 5
            return cnt
        return method2()
# @lc code=end

