class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def valPrnth(stack:list[str], ind:int):
            state = (tuple(stack), ind)
            if state in memo:
                return memo[state]
            if ind == len(s):
                return len(stack) == 0
            if s[ind] == '(':
                res = valPrnth(stack + ['('], ind + 1)
            elif s[ind] == ')':
                if stack and stack[-1] == '(':
                    res = valPrnth(stack[:-1], ind + 1)
                else:
                    res = False
            elif s[ind] == '*':
                res = valPrnth(stack + ['('], ind+1) or valPrnth(stack, ind+1) or (valPrnth(stack[:-1], ind+1) if stack and stack[-1] == '(' else False)
            memo[state] = res
            return res
        return valPrnth([],0)