class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        else:
            l = r = 0
            hmap = {}
            window = {}
            for i in range(len(s1)):
                hmap[s1[i]] = 1 + hmap.get(s1[i], 0)
            print(hmap)
            while r < len(s2):
                window[s2[r]] =1 + window.get(s2[r],0)
                if r - l + 1 > len(s1):
                    if window[s2[l]] == 1:
                       del window[s2[l]]
                    else:
                        window[s2[l]] -= 1
                    l+=1
                if window == hmap:
                    return True
                r+=1
            return False
