class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]
        max_right = [0]
        max_l = max_r = res = 0
        for i in range(1,len(height)):
            max_l = max(max_l,height[i-1])
            max_left.append(max_l)

        for i in range(len(height)-2,-1,-1):
            max_r = max(max_r,height[i+1])
            max_right.append(max_r)
        max_right = max_right[::-1]

        for i in range(len(height)):
            water_at_i = min(max_left[i],max_right[i]) - height[i]
            res+= 0 if  water_at_i < 0 else water_at_i
        
        return res

        


       
                    