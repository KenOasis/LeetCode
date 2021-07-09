from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = max(prices)
        max_profit = 0
        max_accumulate_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit =price - min_price
                max_accumulate_profit += max_profit
                min_price = price
                max_profit = 0
        return max_accumulate_profit

s = Solution()
prices = [1,2,3,4,5,4,5]
print(s.maxProfit(prices))