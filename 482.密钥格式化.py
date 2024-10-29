#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        n = len(s)
        res = []
        cur = []
        for i in range(n-1, -1, -1):
            if s[i] == '-':
                continue
            cur.append(s[i].upper())
            if len(cur) == k:
                res.append(''.join(cur[::-1]))
                cur = []
        if len(cur) != 0:
            res.append(''.join(cur[::-1]))
        return '-'.join(res[::-1])


# @lc code=end

