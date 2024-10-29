#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber != 0:
            columnNumber -= 1
            res.append(chr((columnNumber) % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(res[::-1])
# @lc code=end

