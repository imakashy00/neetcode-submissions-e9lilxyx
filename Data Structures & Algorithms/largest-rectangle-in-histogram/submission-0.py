class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area:int = 0
        for i in range(len(heights)):
            j,k = i,i
            while j >= 0 and  heights[j] >= heights[i] :
                j-=1
            while k <len(heights) and heights[k] >= heights[i]:
                k+=1
            area = max(area,((k-1)-(j+1)+1)*heights[i])
        return area            