# Last updated: 5/27/2026, 11:41:52 AM
1class Solution:
2    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
3        res = []
4        count = 0
5        prev = nums[0]
6
7        for i,v in enumerate(nums):
8            if v == prev:
9                if count < k:
10                    count+=1
11                    res.append(v)
12                else:
13                    pass
14            else:
15                count = 1
16                res.append(v)
17                prev = v
18
19
20        return res
21
22            