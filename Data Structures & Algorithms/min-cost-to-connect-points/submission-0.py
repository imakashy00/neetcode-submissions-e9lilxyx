class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i:[] for i in range(len(points))}

        for i in range(len(points)):
            x, y = points[i]
            for j in range(i+1, len(points)):
                x1, y1 = points[j]
                dis = abs(x1-x)+abs(y1-y)
                adj[i].append([dis,j])
                adj[j].append([dis,i])
        
        res = 0
        visited = set()
        minh = [[0,0]] # starting index and initial cost
        
        while len(visited) < len(points): # N
            cost, point = heapq.heappop(minh) # log N
            if point not in visited:
                res+=cost
                visited.add(point)
                for neigh_cost, neigh in adj[point]:
                    if neigh not in visited:
                        heapq.heappush(minh, [neigh_cost, neigh])
        return res
