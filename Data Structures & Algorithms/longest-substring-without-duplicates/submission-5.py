class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_set = set()
        unique_len = 0
        i = j = 0
        while j<len(s):
            if s[j] not in unique_set:
                unique_set.add(s[j])
                unique_len = max(unique_len,len(unique_set))
                j+=1
            else:
                unique_set.remove(s[i])
                i+=1
            
        return unique_len