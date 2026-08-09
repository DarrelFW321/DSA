# Last updated: 8/8/2026, 10:31:39 PM
1class Solution:
2    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
3        prices.sort(reverse=True)
4        discounts.sort(reverse=True)
5
6        ans = sum(prices)
7
8        for i in range(min(len(prices), len(discounts))):
9            ans -= prices[i] * discounts[i] / 100
10
11        return ans