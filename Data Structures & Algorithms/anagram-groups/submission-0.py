class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp:dict[list[str]] = {}
        for s in strs:
            srt = ''.join(sorted(s))
            if srt in mp:
                mp[srt].append(s)
            else: mp[srt] = [s]
        
        return list(mp.values())
