# Last updated: 9/5/2026, 11:39:50 PM
1class Solution:
2    def countGoodRotations(self, nums: list[int]) -> int:
3        n = len(nums)
4        mid = n // 2
5
6        total = sum(nums)
7        left = sum(nums[:mid])
8
9        res = 0
10
11        for i in range(n):
12            if left > total - left:
13                res += 1
14
15            left -= nums[i]
16
17            left += nums[(i + mid) % n]
18
19        return res
20
21            
22                
23
24            
25                
26            
27        
28
29        