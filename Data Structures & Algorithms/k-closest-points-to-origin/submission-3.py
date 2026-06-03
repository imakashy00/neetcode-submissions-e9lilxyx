import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda item: item[0]*item[0] + item[1]*item[1])
        return points[:k]