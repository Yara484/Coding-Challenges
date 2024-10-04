class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding Window
        # buy has to be smaller than sell
        l, r = 0, 1
        profit = 0
        for i in range(len(prices)-1):
            profit = max(profit, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
            r += 1

        return profit

"""
 0,1,2,3,4,5
[7,1,5,3,6,4]
l = 0, 1
r = 1, 2, 3, 4
profit = 0, 4, 5
"""