# Last updated: 5/24/2026, 4:30:39 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        temp = nums
4        curr = None
5        index = 0
6        for i,v in enumerate (temp):
7            if curr is None or  v > curr:
8                nums[index] = v
9                curr = v
10
11                index+=1
12        return index