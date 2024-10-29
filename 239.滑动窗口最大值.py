#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def method1():
            import heapq
            hp = []
            for i in range(k):
                heapq.heappush(hp, (-nums[i], i))
            ans = [-hp[0][0]]

            for i in range(k, len(nums)):
                while hp and i-hp[0][1]>=k:
                    heapq.heappop(hp)
                heapq.heappush(hp, (-nums[i], i))
                ans.append(-hp[0][0])
            return ans
        def method2():
            from collections import deque
            dq = deque()
            for i in range(k):
                while dq and nums[i] > nums[dq[-1]]:
                    dq.pop()
                dq.append(i)
            ans = []
            ans.append(nums[dq[0]])
            for i in range(k, len(nums)):
                while dq and nums[i] > nums[dq[-1]]:
                    dq.pop()
                dq.append(i)
                if i - dq[0]>=k:
                    dq.popleft()
                ans.append(nums[dq[0]])
            return ans
        return method2()

        
# @lc code=end

