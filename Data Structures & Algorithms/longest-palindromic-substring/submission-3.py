class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPal(sub):
            ind = 0
            for _ in range(len(sub)//2):
                if sub[ind] != sub[len(sub)-1-ind]:
                    return False
                ind+=1
            return sub

        for i in range(len(s)):
        # The inner loop 'j' slides the starting position from left to right
            for j in range(i + 1):
            # Calculate the sliding window slice
            # When i=1, this checks s[0:-1] then s[1:]
                sub = s[j : len(s) - i + j]
                
                if isPal(sub):
                    return sub