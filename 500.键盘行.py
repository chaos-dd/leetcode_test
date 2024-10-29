#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        ans = []
        for w in words:
            for row in rows:
                flag = True
                for c in w:
                    if c.lower() not in row:
                        flag = False
                        break
                if flag:
                    ans.append(w)
                    break
        return ans

        
# @lc code=end

