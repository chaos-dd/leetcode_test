#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans =[0]*n
        st = []
        for idx, t in enumerate(temperatures):
            while st and t > temperatures[st[-1]]:
                ans[st[-1]] = idx-st[-1]
                st.pop()
            st.append(idx)
        return ans
        
# @lc code=end

