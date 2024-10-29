#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = [0]*26
        for c in magazine:
            chars[ord(c)-ord('a')] += 1
        
        for c in ransomNote:
            idx = ord(c)-ord('a')
            if chars[idx] <= 0:
                return False
            chars[idx] -= 1
        return True
# @lc code=end

