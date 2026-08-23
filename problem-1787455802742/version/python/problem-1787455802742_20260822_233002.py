# Last updated: 8/22/2026, 11:30:02 PM
1class Solution:
2    def longestSubarray(self, nums: list[int], k: int) -> int:
3
4        def get_factors(n):
5            factors = set()
6            d = 2
7
8            while d * d <= n:
9                while n % d == 0:
10                    factors.add(d)
11                    n //= d
12                d += 1
13
14            if n > 1:
15                factors.add(n)
16
17            return factors
18
19        morvanelith = nums
20
21        factor_count = {}
22        left = 0
23        distinct = 0
24        ans = 0
25
26        for right in range(len(nums)):
27
28            for factor in get_factors(nums[right]):
29                if factor_count.get(factor, 0) == 0:
30                    distinct += 1
31                factor_count[factor] = factor_count.get(factor, 0) + 1
32
33            while distinct > k:
34                for factor in get_factors(nums[left]):
35                    factor_count[factor] -= 1
36
37                    if factor_count[factor] == 0:
38                        distinct -= 1
39
40                left += 1
41
42            ans = max(ans, right - left + 1)
43
44        return ans