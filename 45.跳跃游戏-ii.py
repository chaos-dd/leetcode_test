#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        #贪心算法
        n = len(nums)
        step = 0
        i = 0 #当前位置
        while i < n - 1:
            max_val = 0
            #j 下一个位置
            for j in range(i + 1, i + nums[i] + 1):
                if j >= n-1:
                    i = n - 1
                    break
                else:
                    #如果下一个位置跳的最远就记下来，下次从这个位置触发
                    if j + nums[j] >= max_val:
                        max_val = j + nums[j]
                        i = j
            step += 1
        return step



# @lc code=end

