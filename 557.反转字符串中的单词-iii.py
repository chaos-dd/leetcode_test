#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s)
        l = 0
        for i in range(len(arr)):
            if arr[i] == ' ' or i == len(arr)-1:
                r = i -1 if arr[i] == ' ' else i
                while l < r:
                    arr[l],arr[r]=arr[r],arr[l]
                    l+=1
                    r-=1
                l = i + 1
        return ''.join(arr)
        
# @lc code=end

