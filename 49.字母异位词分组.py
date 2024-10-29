#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dic = defaultdict(list)
        for word in strs:
            cnt = [0]*26
            for c in word:
                cnt[ord(c)-ord('a')] += 1
            dic[tuple(cnt)].append(word)
        return list(dic.values())
# @lc code=end

