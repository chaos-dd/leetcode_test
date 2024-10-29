#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        cnt = n - 2
        flag = [True] * n
        for i in range(2, n):
            if not flag[i]:
                continue
            for j in range(2*i,n, i):
                if flag[j]:
                    flag[j] = False
                    cnt -= 1
        # print(flag)
        return cnt

# @lc code=end

