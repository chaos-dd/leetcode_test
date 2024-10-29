#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        def method1():
            n=len(height)
            left_max = [0]*n
            for i in range(1, n-1):
                left_max[i] = max(left_max[i-1], height[i-1])
            right_max = [0]*n
            for i in range(n-2, 0, -1):
                right_max[i] = max(right_max[i+1], height[i+1])
            ans = 0
            for i in range(1, n-1):
                ans += max(0, min(left_max[i], right_max[i]) - height[i])
            return ans
        def method2():
            ans = 0
            st = []
            for i in range(len(height)):
                while st and height[i] > height[st[-1]]:
                    bottom = height[st[-1]]
                    st.pop()
                    if not st:
                        break
                    left = height[st[-1]]
                    width = i-st[-1]-1
                    ans += max(0, (min(left, height[i])-bottom)*width)
                st.append(i)
            return ans
        def method3():
            if len(height)<=2:
                return 0
            left_max, right_max = height[0], height[-1]
            left, right = 1, len(height)-2
            ans = 0
            while left <= right:
                if left_max < right_max:
                    ans += max(0, min(left_max, right_max)-height[left])
                    left_max=max(left_max, height[left])
                    left+=1
                else:
                    ans += max(0, min(left_max, right_max)-height[right])
                    right_max=max(right_max,height[right])
                    right-=1
            return ans
        return method3()
        

# @lc code=end

