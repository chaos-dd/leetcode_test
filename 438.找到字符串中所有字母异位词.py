#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        ans = []
        count_s = [0]*26
        count_p = [0]*26
        for c in p:
            count_p[ord(c)-ord('a')] += 1
        for i in range(len(p)):
            c = s[i]
            count_s[ord(c)-ord('a')] += 1
        if count_p == count_s:
            ans.append(0)
        left = 0
        for right in range(len(p), len(s)):
            count_s[ord(s[left])-ord('a')]-=1
            count_s[ord(s[right])-ord('a')] += 1
            left += 1
            if count_s == count_p:
                ans.append(left)
        return ans

