# Last updated: 8/22/2026, 2:15:37 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        st = set(nums)
4        res = 0
5
6        for v in st:
7            if v-1 not in st:
8                curr = 0
9                val = v
10                while val in st:
11                    curr+=1
12                    val+=1
13                res=max(curr,res)
14        return res
15