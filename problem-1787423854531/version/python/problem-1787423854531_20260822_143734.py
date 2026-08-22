# Last updated: 8/22/2026, 2:37:34 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        l = 0
4        r = len(numbers)-1
5
6        while l < r:
7            temp = numbers[l] + numbers[r]
8            if temp == target:
9                return [l+1,r+1]
10            if temp < target:
11                l+=1
12            if temp > target:
13                r-=1