class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0
        def find_pal(l,r,sub):
            nonlocal res,resLen
            while l >= 0 and r < len(sub) and sub[l] == sub[r]:
                if (r - l + 1) > resLen:
                    res = sub[l:r+1]
                    resLen = r - l + 1
                l-=1
                r+=1
            return res
        for i in range(len(s)):
            # odd length pal
            l= r = i
            odd_pal = find_pal(l,r,s)
            # even length pal
            l, r = i, i+1
            even_pal = find_pal(l,r,s)
        return odd_pal if len(odd_pal) > len(even_pal) else even_pal