class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(count_pre, count_pos, st):
            if len(st) == 2*n:
                return res.append(st)
            if count_pre > 0:
                backtrack(count_pre-1, count_pos, st+'(')
            if count_pos > count_pre:
                backtrack(count_pre, count_pos-1, st+')')
        backtrack(n-1,n,'(')
        return res
