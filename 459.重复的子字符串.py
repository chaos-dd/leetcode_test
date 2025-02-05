#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n//2+1):
            if n%i != 0:
                continue
            flag = True
            for j in range(i, n, i):
                if not flag:
                    break
                for k in range(i):
                    # print(i, j, k)
                    if s[k] != s[j+k]:
                        flag = False
                        break
            if flag:
                # print('debug', i)
                return True
        return False


# @lc code=end

