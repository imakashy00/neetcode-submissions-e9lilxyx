class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res:list[int] = []
        for i in range(len(temperatures)-1):
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res.append(j - i)
                    break
                elif j == len(temperatures)-1 and temperatures[j] <= temperatures[i]:
                    res.append(0)
        res.append(0)
        return res

