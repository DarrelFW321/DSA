# Last updated: 8/22/2026, 3:02:33 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums = sorted(nums)
4        st = set()
5        done = set()
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
17            res = []
18            # print ("mid ", nums[i])
19
20            while (l < r):
21                temp = nums [i] + nums[l] + nums[r]
22                if temp == 0:
23                    res.append((nums[l],nums[i],nums[r]))
24                    if nums[l] == nums[l+1]:
25                        l+=1
26                    l+=1
27                if temp > 0:
28                    r-=1
29                if temp < 0:
30                    l+=1
31            return res
32
33
34        for i in range(len(nums)-1):
35            for v in twosum(i):
36                st.add(v)
37
38        res = []
39        for v in st:
40            res.append([v[0],v[1],v[2]])
41        return res
42
43
44