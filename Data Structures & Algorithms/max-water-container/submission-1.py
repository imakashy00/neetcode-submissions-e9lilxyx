class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water:int = 0
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                max_water = max(max_water,(min(heights[i],heights[j])*(j-i)))
        return max_water
