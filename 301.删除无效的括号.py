#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        lnum, rnum = 0,0
        for c in s:
            if c =='(':
                lnum += 1
            if c == ')':
                rnum += 1
        max_cnt = min(lnum, rnum)
        ans = set()
        max_len = 0
        def dfs(idx, cur, cnt):
            nonlocal ans, max_len
            if cnt < 0 or cnt > max_cnt:
                return
            if idx >= len(s):
                if cnt == 0 and len(cur)>=max_len:
                    if len(cur)>max_len:
                        ans.clear()
                        max_len = len(cur)
                    ans.add(cur)
                return 
            if s[idx] == '(':
                dfs(idx+1, cur+s[idx], cnt+1)
                dfs(idx+1, cur, cnt)
            elif s[idx] == ')':
                dfs(idx+1, cur+s[idx], cnt-1)
                dfs(idx+1, cur, cnt)
            else:
                dfs(idx+1, cur+s[idx], cnt)
        dfs(0, '', 0)
        return list(ans)


        
# @lc code=end

