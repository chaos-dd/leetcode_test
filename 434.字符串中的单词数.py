#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        cnt = 0
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                if start != i:
                    cnt += 1
                start = i + 1
        if start != len(s):
            cnt += 1
        return cnt
# @lc code=end

