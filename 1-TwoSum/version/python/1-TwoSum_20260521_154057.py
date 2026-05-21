# Last updated: 5/21/2026, 3:40:57 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        mp = {}
4
5        for i,v  in enumerate (nums):
6            needed = target - v
7            if needed in mp:
8                return [i,mp[needed]]
9            mp[v] = i
10
11        