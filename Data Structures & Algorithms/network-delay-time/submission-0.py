class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))
        minHeap = [(0,k)]
        visit = set()
        time = 0
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            time = max(time, weight)
            for neigh, neigh_weight in edges[node]:
                if neigh not in visit:
                    heapq.heappush(minHeap,(neigh_weight+weight, neigh))
        return time if len(visit) == n else -1