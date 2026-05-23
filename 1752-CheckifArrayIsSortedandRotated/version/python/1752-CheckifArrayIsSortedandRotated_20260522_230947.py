# Last updated: 5/22/2026, 11:09:47 PM
1class Solution:
2    def check(self, nums: List[int]) -> bool:
3        drops = 0
4
5        for i in range(len(nums)):
6            if nums[i] > nums[(i + 1) % len(nums)]:
7                drops += 1
8
9        return drops <= 1