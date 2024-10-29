#
# @lc app=leetcode.cn id=307 lang=python3
#
# [307] 区域和检索 - 数组可修改
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0]*(len(nums)+1)
        for i in range(1, len(nums)+1):
            self.prefix[i] = self.prefix[i-1]+nums[i-1]

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        for i in range(index+1, len(self.nums)+1):
            self.prefix[i] = self.prefix[i-1]+self.nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end

