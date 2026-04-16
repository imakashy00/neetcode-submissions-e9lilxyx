class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        # Append 0 to heights to ensure the stack is fully emptied at the end
        heights.append(0)
        
        for i, h in enumerate(heights):
            # When current bar is shorter than the stack top, we've found
            # the right boundary for the bar at stack[-1]
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                # If stack is empty, the bar was the shortest so far (width is i)
                # Otherwise, width is the distance between i and the new stack top
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            
            stack.append(i)
            
        # Restore heights list (optional)
        heights.pop()
        return max_area
