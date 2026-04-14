class Solution:
    def isValid(self, s: str) -> bool:
        stack:list[str] = []
        hmap={'(':')','{':'}','[':']'}
        for char in s:
            if stack and hmap.get(stack[-1]) == char:
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0 