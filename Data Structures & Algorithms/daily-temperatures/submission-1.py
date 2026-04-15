class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res:list[int] = [0]*len(temperatures)
        stack:list[int] = []
        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                p_ind = stack.pop()
                res[p_ind]= (i-p_ind)
            stack.append(i)
        return res

