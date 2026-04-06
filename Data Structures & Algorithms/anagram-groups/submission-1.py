class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp:dict[tuple,list[str]] = {}
        for s in strs:
            count:list[int] = [0]*26
            for i in range(len(s)):
                count[ord(s[i])-ord('a')]+=1
            if tuple(count) in mp:
                mp[tuple(count)].append(s)
            else: mp[tuple(count)] = [s]
        return list(mp.values())