#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import defaultdict
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        
        res = 0
        flag = False
        for c, cnt in dic.items():
            res += cnt//2 * 2
            if not flag and cnt % 2 == 1:
                flag = True
                res += 1
        return res

# @lc code=end

