class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t) :
            return False
        score = {}
        for i in range(len(s)):
            if s[i] in score:
                score[s[i]]+=1
            else: 
                score[s[i]] = 1
            if t[i] in score:
                score[t[i]]-=1
            else :
                score[t[i]] = -1
        if set(score.values())=={0}:
            return True
        return False



        