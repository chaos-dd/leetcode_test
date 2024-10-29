#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        def method1():
            pre, cur = 0, 1
            ans = 0
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    cur += 1
                else:
                    pre = cur
                    cur = 1
                if pre >= cur:#很关键
                    ans += 1
            return ans
        def method2():
            ans = 0
            count = []
            cur = 1
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    cur += 1
                else:
                    count.append(cur)
                    cur = 1
            count.append(cur)
            for i in range(1, len(count)):
                ans += min(count[i-1], count[i])
            return ans
        return method2()
# @lc code=end

