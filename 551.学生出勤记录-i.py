#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt_a = 0
        cnt_l = 0
        for i in range(len(s)):
            if s[i] == 'A':
                cnt_a += 1
            if cnt_a >= 2:
                return False
            if s[i] == 'L':
                cnt_l += 1
                if cnt_l >= 3:
                    return False
            else:
                cnt_l = 0
        return True
        
# @lc code=end

