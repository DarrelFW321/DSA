# Last updated: 8/22/2026, 2:59:18 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums = sorted(nums)
4        st = set()
5        done = set()
6        # print (nums)
7        
8        def twosum(i):
9            if i in done:
10                return []
11            else:
12                done.add(i)
13            if i >= len(nums)-2:
14                return []
15            l = i+1
16            r = len(nums)-1
17            res = []
18            # print ("mid ", nums[i])
19
20            while (l < r):
21                temp = nums [i] + nums[l] + nums[r]
22                if temp == 0:
23                    res.append((nums[l],nums[i],nums[r]))
24                    l+=1
25                if temp > 0:
26                    r-=1
27                if temp < 0:
28                    l+=1
29            return res
30
31
32        for i in range(len(nums)-1):
33            for v in twosum(i):
34                st.add(v)
35
36        res = []
37        for v in st:
38            res.append([v[0],v[1],v[2]])
39        return res
40
41
42