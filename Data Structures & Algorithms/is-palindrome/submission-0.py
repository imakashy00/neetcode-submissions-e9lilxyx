class Solution:
    def isPalindrome(self, s: str) -> bool:
        palStr:str = ''
        for char in s:
            if char.isalnum():
                palStr+=char.lower()
        print(palStr)
        if palStr[::-1] == palStr:
            return True
        return False