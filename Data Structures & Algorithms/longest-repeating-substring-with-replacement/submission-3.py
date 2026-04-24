class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = i = maxf = 0
        hmap = {}
        for j in range(len(s)):
            hmap[s[j]] = 1 + hmap.get(s[j],0)
            maxf = max(maxf,hmap[s[j]])
            if j - i + 1 - maxf > k:
                hmap[s[i]] -= 1
                i+=1
            res = max(res,j - i + 1)
        return res


