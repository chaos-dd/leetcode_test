#
# @lc app=leetcode.cn id=318 lang=python3
#
# [318] 最大单词长度乘积
#

# @lc code=start
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        from collections import defaultdict
        bits = []
        for word in words:
            v = 0
            for c in word:
                idx = ord(c)-ord('a')
                v |= (1<<idx)
            bits.append(v)
        ans = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if (bits[i] & bits[j]) != 0:
                    continue
                ans = max(ans, len(words[i]) * len(words[j]))
        return ans

# @lc code=end

