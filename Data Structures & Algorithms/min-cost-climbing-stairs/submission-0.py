class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        hmap = {0:cost[0],1:cost[1]}
        def climb(step):
            if step in hmap:
                return hmap[step]
            else:
                curr_cost = cost[step] if step < len(cost) else 0
                hmap[step] = min(climb(step-1), climb(step-2)) + curr_cost
                return hmap[step]
        climb(len(cost))
        return hmap[len(cost)]