# Last updated: 9/26/2026, 11:39:30 PM
1class Solution:
2    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
3
4
5        consecutive = defaultdict(int)
6        unordered = defaultdict(int)
7        for i,v in enumerate(nums):
8            if i == len(nums)-1:
9                break
10            if nums[i] == nums[i+1]:
11                consecutive[nums[i]]+=1
12            else:
13                unordered[(min(nums[i], nums[i+1]), max(nums[i], nums[i+1]))] += 1
14
15        curr = sum(consecutive.values())
16
17        best = 0
18
19        for cnt in unordered.values():
20            best = max(best, cnt)
21
22        return curr+best
23        
24
25        
26            