class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hmap = {}
        def dfs(curr_sum):
            if curr_sum == 0:
                return 0
            if curr_sum < 0:
                return float('inf')
            if curr_sum in hmap:
                return hmap[curr_sum]

            min_coins = float('inf')
            for coin in coins:
                min_coins = min(min_coins, 1 + dfs(curr_sum - coin))
            hmap[curr_sum] = min_coins
            return hmap[curr_sum]
        res = dfs(amount)
        return -1 if res == float('inf') else res
        

            