#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = [0]*26
        for c in s:
            chars[ord(c) - ord('a')] += 1
        for i, c in enumerate(s):
            if chars[ord(c)-ord('a')] == 1:
                return i
        return -1

# @lc code=end

