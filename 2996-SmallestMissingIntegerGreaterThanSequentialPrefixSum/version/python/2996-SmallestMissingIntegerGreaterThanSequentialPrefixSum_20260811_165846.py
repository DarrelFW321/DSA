# Last updated: 8/11/2026, 4:58:46 PM
1class Solution:
2    def missingInteger(self, nums: List[int]) -> int:
3        total = nums[0]
4
5        for i in range(1,len(nums)):
6            if nums[i] == nums[i-1]+1:
7                total+=nums[i]
8            else:
9                break
10
11        seen = set (nums)
12
13        while total in seen:
14            total+=1
15
16        return total
17