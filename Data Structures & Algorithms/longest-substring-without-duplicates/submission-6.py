class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = {}
        i = res = 0
        for j in range(len(s)):
            if s[j] in hmap:
                i = max(hmap[s[j]]+1,i)
            hmap[s[j]] = j
            res = max(res,j-i+1)
        return res
