class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0]*3
        for tri in triplets:
            if tri[0] > target[0] or tri[1] > target[1] or tri[2] > target[2]:
                continue 
            for i, value in enumerate(tri):
                if value == target[i]:
                    res[i] = value
        return res == target