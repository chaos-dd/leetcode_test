#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        mapping = {'2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'}

        ans = []
        cur = []
        def bt(idx):
            if idx >= len(digits):
                ans.append(''.join(cur[:]))
                return
            for c in mapping[digits[idx]]:
                cur.append(c)
                bt(idx+1)
                cur.pop()
        bt(0)
        return ans


# @lc code=end

