from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=max(prices)
        maxprofit=0
        for price in prices:
            if price<minprice: 
                minprice=price
            profit = price-minprice
            if profit>maxprofit:
                maxprofit=profit
        return maxprofit
def test():
    s = Solution()
    prices = [7,1,5,3,6,4]
    max_profit = s.maxProfit(prices)
    assert max_profit == 5
                    