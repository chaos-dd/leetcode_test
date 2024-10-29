#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        from collections import defaultdict
        dic = defaultdict(int)
        cnt = 0
        for c in t:
            cnt += 1
            dic[c] += 1

        l = 0
        ans = ''
        min_len = float('inf')
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] -= 1
                if dic[s[i]] >= 0:
                    cnt -= 1
            while l<i:
                if s[l] not in dic:
                    l += 1
                elif dic[s[l]] < 0:
                    dic[s[l]] += 1
                    l += 1
                else:
                    break
            if cnt == 0:
                if i-l+1<min_len:
                    ans = s[l:i+1]
                    min_len = len(ans)
        return ans

# @lc code=end

