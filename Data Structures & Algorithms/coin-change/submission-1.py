class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hmap = {}
        def dfs(ind, curr_sum):
            if curr_sum == 0:
                return 0
            if curr_sum < 0 or ind == len(coins):
                return float('inf')
            if (ind, curr_sum) in hmap:
                return hmap[(ind,curr_sum)]

            select = 1 + dfs(ind, curr_sum - coins[ind])
            not_select = dfs(ind+1,curr_sum)
            hmap[(ind,curr_sum)] = min(select, not_select)
            return hmap[(ind, curr_sum)]
        res_coins = dfs(0,amount)
        return -1 if res_coins == float('inf') else res_coins