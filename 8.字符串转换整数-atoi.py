#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        flag = 0
        res = 0
        max = 2**31-1
        min = -2**31
        for i in range(len(s)):
            if s[i] == ' ':
                if flag == 0:
                    continue
                else:
                    break
            if flag != 0 and (s[i] == '+' or s[i] == '-'):
                break
            if s[i] == '+':
                flag = 1
            elif s[i] == '-':
                flag = -1
            elif s[i].isdigit():
                if flag == 0:
                    flag = 1
                cur = ord(s[i]) - ord('0')
                if flag == 1 and (max - cur)/10 < res:
                    res = max
                    break
                elif flag == -1 and res > (flag * min-cur)/10:
                    res = flag * min
                    break
                else:
                    res = res*10 + cur
            else:
                break
        return flag * res
        
# @lc code=end

