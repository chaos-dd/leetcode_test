#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def method1():
            ans = 0
            st = [-1]
            for i in range(len(s)):
                if s[i]=='(':
                    st.append(i)
                else:
                    st.pop()
                    if not st:
                        st.append(i)
                    else:
                        ans = max(ans, i-st[-1])
            return ans


        def method2():
            if len(s) == 0:
                return 0
            n = len(s)
            dp = [0]*n
            for i in range(1, n):
                if s[i] == '(':
                    continue
                if s[i-1] == '(':
                    dp[i] = 2
                    if i -2>=0:
                        dp[i]+=dp[i-2]
                else:
                    #如果dp[i-1]==0，其实已经不合法了
                    #这时候idx=i-1，s[idx] 肯定不等于(，
                    #因为已经在上面的if里了
                    #整体也进不去
                    idx = i-dp[i-1]-1
                    if idx>=0 and s[idx]=='(':
                        dp[i] = dp[i-1]+2
                        if idx > 0:
                            dp[i]+=dp[idx-1]
            return max(dp)
        
        return method3()

# @lc code=end

