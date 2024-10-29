#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        r, c = 0, 0
        for m in moves:
            if m=='R':
                c+=1
            elif m == 'L':
                c-=1
            elif m == 'U':
                r-= 1
            else:
                r+=1
        return r == 0 and c == 0
        
# @lc code=end

