class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = i = j = maxf = 0
        hmap = {}
        while j < len(s):
            print(hmap,i,j,s[j],maxf,res)
            hmap[s[j]] = 1 + hmap.get(s[j],0)
            maxf = max(maxf,hmap[s[j]])
            if j - i + 1 - maxf <= k:
                res = max(res,j - i + 1)
            else:
                hmap[s[i]] = hmap.get(s[i]) - 1
                i+=1
            j+=1
        return res


