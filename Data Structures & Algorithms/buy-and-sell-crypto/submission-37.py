class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = 0
        y = prices[0]
        for sell in prices:
            x = max(x,sell-y)
            y = min(y,sell)
        return x