class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        profits.append(0)
        big = prices[0]
        smo = prices[0]
        for i in prices:
            if i < smo:
                smo = i
                big = i
            elif i> big:
                big = i
                profits.append(big-smo)
        return max(profits)