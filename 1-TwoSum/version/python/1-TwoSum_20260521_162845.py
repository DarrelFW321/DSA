# Last updated: 5/21/2026, 4:28:45 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        buckets = [[] for _ in range (len(nums)+1)]
4        mp = {} # key is num, value is count
5        for num in nums:
6            mp[num] = mp.get(num,0) + 1
7
8        for key,val in mp.items():
9            if len(buckets[val]) == 0:
10                buckets[val] = [key]
11            else:
12                buckets[val].append(key)
13
14
15        res = []
16        count = 0
17
18        for i in range (len(nums),0 , -1):
19            for num in buckets[i]:
20                res.append(num)
21                count+=1
22            if (count ==  k):
23                return res
24