#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        ex = 0
        i, j = len(a)-1, len(b)-1
        while i >= 0 or j >= 0 or ex > 0:
            val = ex
            if i >= 0:
                val += ord(a[i]) - ord('0')
            if j >= 0:
                val += ord(b[j]) - ord('0')
            ex = val // 2
            val = val % 2
            res.append(val)
            i -= 1
            j -= 1
        return ''.join(map(str, res[::-1]))
# @lc code=end

