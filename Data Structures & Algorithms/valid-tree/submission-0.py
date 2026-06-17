class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hmap = { node:[] for node in range(n)}
        for start, end in edges:
            hmap[start].append(end)
            hmap[end].append(start)
        visited = set()

        def dfs(node,parent):
            if node in visited: return False
            visited.add(node)
            for neigh in hmap[node]:
                if neigh == parent: continue
                if not dfs(neigh, node): return False

            return True

        if not dfs(0, -1): return False
        return len(visited) == n