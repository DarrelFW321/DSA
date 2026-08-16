# Last updated: 8/16/2026, 4:31:06 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        mp = {}
4
5        for i,v in enumerate(nums):
6            x = target-v
7            if x in mp:
8                return [mp[x],i]
9            else:
10                mp[v] = i
11
12        return [0,1]
13
14        