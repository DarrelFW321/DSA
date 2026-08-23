# Last updated: 8/22/2026, 11:24:36 PM
1class Solution:
2    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
3        st = set(nums)
4        res = []
5
6        i = lower
7
8        while i <= upper:
9            if i in st:
10                i+=1
11                continue
12            curr = i
13            while curr not in st and curr <= upper:
14                curr+=1
15            res.append([i,curr-1])
16
17            i = curr
18
19        return res
20            