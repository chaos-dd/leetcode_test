#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        def method1():
            cnt = 1
            flag = True
            for i in range(1, len(nums)):
                # print(i, cnt, flag)
                if nums[i] < nums[i-1]:
                    if cnt == 0:
                        flag = False
                        break
                    f1, f2 = True, True
                    #改小前一个
                    if i > 1 and nums[i] < nums[i-2]:
                        f1 = False
                    #改大当前的
                    if i < len(nums) - 1 and nums[i-1] > nums[i+1]:
                        f2 = False
                    flag = f1 or f2
                    if not flag:
                        break
                    cnt -= 1
            return flag
        return method1()

# @lc code=end

