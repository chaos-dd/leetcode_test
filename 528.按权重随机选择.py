#
# @lc app=leetcode.cn id=528 lang=python3
#
# [528] 按权重随机选择
#

# @lc code=start
import random
import bisect
class Solution:

    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.prob = []
        cur = 0
        for i in range(len(w)):
            cur += w[i]
            self.prob.append(cur)
    def pickIndex(self) -> int:
        prob = random.randint(1, self.total)
        return bisect.bisect_left(self.prob, prob)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

