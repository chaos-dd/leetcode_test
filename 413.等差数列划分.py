#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#

# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        #因为等差子序列可能以每个元素结尾
        # 所以dp是以i为结尾的等差子序列
        dp = [0]*n
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1]-nums[i-2]:
                #1是本次判断的这3个数字是等差子序列
                #然后如果本次3个以及是等差了
                # 说明只要前面一个结尾的是等差的，这个差值一定等于最近两个元素的差
                # 所以加上最后一个元素还是等差
                dp[i] = dp[i-1] + 1
        return sum(dp)


# @lc code=end

