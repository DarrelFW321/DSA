# Last updated: 8/22/2026, 2:54:27 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums = sorted(nums)
4        st = set()
5        # print (nums)
6        
7        def twosum(i):
8            l = 0
9            r = len(nums)-1
10            res = []
11            # print ("mid ", nums[i])
12
13            while (l < i and r>i):
14                temp = nums [i] + nums[l] + nums[r]
15                if temp == 0:
16                    res.append((nums[l],nums[i],nums[r]))
17                    l+=1
18                if temp > 0:
19                    r-=1
20                if temp < 0:
21                    l+=1
22            return res
23
24
25        for i in range(1,len(nums)-1):
26            for v in twosum(i):
27                st.add(v)
28
29        res = []
30        for v in st:
31            res.append([v[0],v[1],v[2]])
32        return res
33
34
35