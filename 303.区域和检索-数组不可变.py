#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.presum = [0]
        s = 0
        for i in nums:
            s += i
            self.presum.append(s)

    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right+1] - self.presum[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

