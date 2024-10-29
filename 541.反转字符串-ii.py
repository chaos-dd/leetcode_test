#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        for i in range(0, len(arr), 2*k):
            l, r = i, min(len(arr)-1, i+k-1)
            while l<r:
                arr[l], arr[r]=arr[r],arr[l]
                l += 1
                r -= 1
        return ''.join(arr)

        
# @lc code=end

