class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack:list[str] = []
        tokens = tokens[::-1]
        while tokens:
            print(tokens,stack)
            pop = tokens.pop()
            print(pop)
            if pop == '+':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(op1) + int(op2))
            elif pop == '-':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(op1) - int(op2))
            elif pop == '*':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(op1) * int(op2))
            elif pop == '/':
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(op1) / int(op2))
            else :
                stack.append(pop)
                print(stack)
        return int(stack.pop())
