class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        added, visited = set(), set()
        count = 0
        hmap = {node:[] for node in range(n)}
        for start, end in edges:
            hmap[start].append(end)
            hmap[end].append(start)
        def dfs(i):
            if i in visited: return
            visited.add(i)
            added.add(i)
            for neigh in hmap[i]:
                dfs(neigh)
        for i in range(n):
            if i not in added:
                count+=1
                dfs(i)
        return count