from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, missing = Counter(t), len(t)
        i = start = end = 0
        
        for j, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            
            if missing == 0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                
                if end == 0 or j - i < end - start:
                    start, end = i, j
                    
        return s[start:end]
