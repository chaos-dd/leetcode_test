#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        def method1():
            s = s.replace(' ', '')
            ls = []
            l, r = 0, 0
            while l <= r and r < len(s):
                if s[r] in '+-*/':
                    ls.append(int(s[l:r]))
                    ls.append(s[r])
                    l = r+1
                    r = r+1
                else:
                    r += 1
            ls.append(int(s[l:r]))

            st = []
            pre = '+'
            for i in range(len(ls)):
                if type(ls[i]) is int:
                    if pre == '+':
                        st.append(ls[i])
                    if pre == '-':
                        st.append(-ls[i])
                    if pre == '*':
                        st.append(st.pop()*ls[i])
                    if pre == '/':
                        st.append(int(st.pop() / ls[i]))
                else:
                    pre = ls[i]
            # print(st)
            return sum(st)
        
        def method2():
            nonlocal s
            s = s.replace(' ', '')
            st = []
            pre = '+'
            num = 0
            for i in range(len(s)):
                tmp = ord(s[i]) - ord('0')
                if 0<= tmp  < 10:
                    num = num * 10 + tmp
                if i == len(s) -1 or tmp >= 10 or tmp < 0:
                    if pre == '+':
                        st.append(num)
                    if pre == '-':
                        st.append(-num)
                    if pre == '*':
                        st.append(st.pop() * num)
                    if pre == '/':
                        st.append(int(st.pop()/num))
                    pre = s[i]
                    num = 0
            return sum(st)
        return method2()
                

# @lc code=end

