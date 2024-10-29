#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ex = 1
        ans = []
        for i in range(len(digits)-1, -1, -1):
            val = ex
            val += digits[i]
            ex = val // 10
            val %= 10
            ans.append(val)
        if ex > 0:
            ans.append(ex)
        return ans[::-1]

# @lc code=end

