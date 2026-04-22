class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit:int = 0
        i, j = 0, 1
        while j < len(prices):
            print(prices[j] , prices[j-1])
            if prices[j] > prices[i] :
                profit = max(profit,prices[j] - prices[i])
            else:
                i = j
            j+=1
        return profit
