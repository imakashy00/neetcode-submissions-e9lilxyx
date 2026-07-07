class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = avl_gas = 0
        for i in range(len(gas)):
            avl_gas += gas[i] - cost[i]
            if avl_gas < 0:
                start = i+1
                avl_gas = 0
        return start