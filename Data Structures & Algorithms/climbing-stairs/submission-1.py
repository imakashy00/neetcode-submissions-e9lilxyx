class Solution:
    def climbStairs(self, n: int) -> int:
        hmap = {1:1,2:2}
        def combination(num):
            if num in hmap: # if num is present in dict then returnr that value
                return hmap[num]
            else:
                hmap[num] =  combination(num-1) + combination(num-2) # else compute it
                return hmap[num] # then return
        return combination(n)