#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        is_cap = lambda c: ord('A')<=ord(c) <=ord('Z')

        first = False
        cap_num = 0
        for i in range(len(word)):
            if is_cap(word[i]):
                cap_num += 1
                if i == 0:
                    first = True
        return cap_num == len(word) or cap_num == 0 or (first and cap_num==1)
            




        
# @lc code=end

