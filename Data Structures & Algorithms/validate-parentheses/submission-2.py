class Solution:
    def isValid(self, s: str) -> bool:
        stack:list[str] = []
        hmap = {'(':')','{':'}','[':']'}
        for char in s:
            print(stack)
            if len(stack) > 0:
                if stack[-1] == '(' and char == ')':
                    stack.pop()
                elif stack[-1] == '{' and char == '}':
                    stack.pop()
                elif stack[-1] == '[' and char == ']':
                    stack.pop()
                else:
                    stack.append(char)
            else: 
                stack.append(char)
                
        return len(stack) == 0