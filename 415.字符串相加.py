#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1)-1, len(num2)-1
        res = []
        ex = 0
        while i >=0 or j >=0 or ex != 0:
            tmp = ex
            if i >= 0:
                tmp += ord(num1[i]) - ord('0')
            if j >= 0:
                tmp += ord(num2[j]) - ord('0')
            ex = tmp//10
            tmp %= 10
            res.append(tmp)
            i -= 1
            j -= 1
        return ''.join(map(str, res[::-1]))


# @lc code=end

