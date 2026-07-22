class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minCost = prices[0]
        for i in range(len(prices)):
            #check if profit is better if we sell at this index
            profit = max(profit, prices[i] - minCost)
            if minCost > prices[i]:
                minCost = prices[i]
        return profit
