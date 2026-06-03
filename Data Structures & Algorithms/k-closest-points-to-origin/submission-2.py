import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp_points = [(-(x**2 + y**2), [x, y]) for x, y in points]
        heapq.heapify(hp_points)
        while len(hp_points) > k:
            dis, point = heapq.heappop(hp_points)
        points = [y for x,y in hp_points]
        return points