#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in range(len(s)):
            if s[i] in '([{':
                st.append(s[i])
            else:
                if len(st) == 0:
                    return False
                if s[i] == ')' and st[-1] != '(':
                    return False
                if s[i] == ']' and st[-1] != '[':
                    return False
                if s[i] == '}' and st[-1] != '{':
                    return False
                st.pop()
        return len(st) == 0

        
# @lc code=end

