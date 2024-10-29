#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        n=len(s)

        def dfs(idx):
            if idx >=n:
                return '', n
            res = ''
            num = 0
            while idx<n:
                if s[idx].isdigit():
                    num = num*10 + ord(s[idx])-ord('0')
                    idx+=1
                elif s[idx] == '[':
                    sub_res, idx = dfs(idx+1)
                    res += sub_res*num
                    num = 0
                elif s[idx] == ']':
                    return res, idx+1
                else:
                    res += s[idx]
                    idx += 1
            return res, n
        return dfs(0)[0]

        
# @lc code=end

