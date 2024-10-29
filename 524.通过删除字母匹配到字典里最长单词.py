#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#

# @lc code=start
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def method1():
            res = ''
            for t in dictionary:
                i, j = 0, 0
                while i < len(t) and j < len(s):
                    if t[i] == s[j]:
                        i += 1
                    j += 1
                if i != len(t):
                    continue
                elif len(t) > len(res) or (len(t) == len(res) and t < res):
                    res = t
            return res
        def method2():
            dictionary.sort(key=lambda x:(-len(x), x))
            res = ''
            for t in dictionary:
                i, j = 0, 0
                while i < len(t) and j < len(s):
                    if t[i] == s[j]:
                        i += 1
                    j += 1
                if i == len(t):
                    return t
            return res
        def method3():
            m = len(s)
            f = [[0]*26 for _ in range(m)]
            f.append([m]*26)
            for i in range(m-1, -1, -1):
                for j in range(26):
                    if ord(s[i])-97 == j:
                        f[i][j] = i
                    else:
                        f[i][j] = f[i+1][j]
            res = ''
            for t in dictionary:
                match = True
                i = 0
                for j in range(len(t)):
                    i = f[i][ord(t[j])-97]
                    if i == m:
                        match = False
                        break
                    i += 1
                if match:
                    if len(t) > len(res) or (len(t) == len(res) and t < res):
                        res = t
                    # print(res)
            return res
        return method3()

    
# @lc code=end

