class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Using two pointers, l is buy and r is sell
        res = 0
        l, r = 0, 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            res = max(res, profit)
            if prices[r] < prices[l]:
                l = r
            r += 1
        return res            