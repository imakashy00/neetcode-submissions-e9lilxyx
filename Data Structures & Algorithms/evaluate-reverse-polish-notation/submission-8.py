class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': lambda x, y : x + y,
            '-': lambda x, y : x - y,
            '*': lambda x, y : x * y,
            '/': lambda x,y : int(x / y)
        }
        tokens=tokens[::-1]
        stack:list[int]=[]
        while tokens:
            pop:str = tokens.pop()
            if pop in ['+','-','*','/']:
                op2:str = stack.pop()
                op1:str = stack.pop()
                stack.append(ops[pop] (op1,op2))
            else:
                stack.append(int(pop))
        return int(stack.pop())