# Last updated: 8/8/2026, 10:33:26 PM
1class Solution:
2    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
3        prices.sort(reverse=True)
4        discounts.sort(reverse=True)
5
6        ans = 0
7        for v in prices:
8            ans += v
9
10        length = min(len(prices), len(discounts))
11
12        for i in range(length):
13            ans -= prices[i] * discounts[i] / 100
14
15        return ans