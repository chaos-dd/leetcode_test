#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1
        n1, n2, n3 = 0, 1, 1
        i = 3
        while i <= n:
            n1, n2, n3 = n2, n3, n1+n2+n3
            i += 1
        return n3
# @lc code=end

