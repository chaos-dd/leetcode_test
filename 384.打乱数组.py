#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#

# @lc code=start
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.ori_data = nums[:]
        self.data = nums[:]
    def reset(self) -> List[int]:
        self.data = self.ori_data[:]
        return self.data
    def shuffle(self) -> List[int]:
        # idx1 = random.randint(0, len(self.data)-1)
        # idx2 = random.randint(0, len(self.data)-1)
        # self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]
        # return self.data
        for i in range(len(self.data)):
            idx = random.randint(i, len(self.data)-1)
            self.data[i], self.data[idx] = self.data[idx], self.data[i]
        return self.data

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

