#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x:(-x[0], x[1]))
        ans = []
        for p in people:
            if p[1] >= len(ans):
                ans.append(p)
            else:
                ans.insert(p[1], p)
        return ans
        
# @lc code=end

