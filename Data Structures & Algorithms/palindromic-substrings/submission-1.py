class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        llen = 0
        rlen = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
                if (r - l + 1) > llen:
                    res+=1
            a, b = i, i+1
            while a >= 0 and b < len(s) and s[a] == s[b]:
                a-=1
                b+=1
                if (b - a + 1) > rlen:
                    res+=1
        return res
                