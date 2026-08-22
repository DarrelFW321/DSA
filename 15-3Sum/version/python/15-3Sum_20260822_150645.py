# Last updated: 8/22/2026, 3:06:45 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums = sorted(nums)
4        done = set()
5        res =[]
6        # print (nums)
7        
8        def twosum(i):
9            if nums[i] in done:
10                return []
11            else:
12                done.add(nums[i])
13            if i >= len(nums)-2:
14                return []
15            l = i+1
16            r = len(nums)-1
17            # print ("mid ", nums[i])
18
19            while (l < r):
20                temp = nums [i] + nums[l] + nums[r]
21                if temp == 0:
22                    res.append([nums[i], nums[l], nums[r]])
23
24                    l += 1
25                    r -= 1
26
27                    while l < r and nums[l] == nums[l - 1]:
28                        l += 1
29
30                    while l < r and nums[r] == nums[r + 1]:
31                        r -= 1
32                if temp>0:
33                    r-=1
34                if temp < 0:
35                    l+=1
36
37
38
39        for i in range(len(nums)-1):
40            twosum(i)
41
42        return res
43
44