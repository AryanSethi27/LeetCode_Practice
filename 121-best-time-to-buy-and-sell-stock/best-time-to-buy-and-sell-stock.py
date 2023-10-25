class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        smo = prices[0]
        for i in prices:
            if i < smo:
                smo = i
            else:
                profit = max(profit, i-smo)
        return profit