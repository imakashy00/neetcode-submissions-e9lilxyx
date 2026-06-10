"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hmap = {}
        def dfs(node):
            if not node: return None
            if node in hmap: return hmap[node]

            hmap[node] = Node(node.val)
            hmap[node].neighbors = [dfs(nei) for nei in node.neighbors]
            return hmap[node]
        return dfs(node)