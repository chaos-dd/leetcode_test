#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        for i in range(len(list2)):
            dic[list2[i]] = i
        ans = []
        min_v = len(list1)+len(list2)
        for i, s in enumerate(list1):
            if s in dic and i+dic[s]<=min_v:
                if i+dic[s]<min_v:
                    min_v = i + dic[s]
                    ans.clear()
                ans.append(s)
        return ans

        
# @lc code=end

