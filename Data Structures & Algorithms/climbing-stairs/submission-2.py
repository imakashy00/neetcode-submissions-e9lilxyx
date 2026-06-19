class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        last, sec_last = 2, 1
        comb = 3
        for i in range(3, n+1):
            comb = last + sec_last
            last, sec_last = comb, last 
        return comb