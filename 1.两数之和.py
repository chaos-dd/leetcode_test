#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        res = [-1,-1]
        for i in range(len(nums)):
            if target-nums[i] in dic:
                return [i, dic[target-nums[i]]]
            else:
                dic[nums[i]] = i
        return res
# @lc code=end

