#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        res = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]+1:
                if start == nums[i-1]:
                    res.append(str(start))
                else:
                    res.append(f'{start}->{nums[i-1]}')
                start = nums[i]
        if start == nums[-1]:
            res.append(str(start))
        else:
            res.append(f'{start}->{nums[-1]}')
        return res
# @lc code=end

