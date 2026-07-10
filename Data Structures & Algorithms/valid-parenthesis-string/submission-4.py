class Solution:
    def checkValidString(self, s: str) -> bool:
        brack = []
        star = []
        
        for i in range(len(s)):
            elem = s[i]
            if elem == "(":
                brack.append(i)
            elif elem == "*":
                star.append(i)
            else:
                if brack:
                    brack.pop()
                elif star:
                    star.pop()
                else:
                    return False
                    
        while brack and star:
            if brack[-1] > star[-1]:
                return False
            brack.pop()
            star.pop()
            
        return len(brack) == 0