class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        big = prices[0]
        smo = prices[0]
        for i in prices:
            if i < smo:
                smo = i
                big = i
            elif i> big:
                big = i
                profit = max(profit, big-smo)
        return profit