class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > buy_price:
                profit += prices[i] - buy_price

            buy_price = prices[i]

        return profit
        