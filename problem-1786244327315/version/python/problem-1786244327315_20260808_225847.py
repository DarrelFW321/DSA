# Last updated: 8/8/2026, 10:58:47 PM
1class Solution:
2    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
3        mp = {}
4        #map of node to depth
5        
6        parentmp = {}
7        # map of parent to list of children
8
9        for i,v in enumerate(parent):
10            if v not in parentmp:
11                parentmp[v] = []
12            parentmp[v].append(i)
13
14        res = 0
15
16        maxdepth= 0
17        
18        def dfs(node,depth):
19            nonlocal maxdepth
20            mp[node] = depth+1
21            if node not in parentmp:
22                maxdepth = max(maxdepth,depth+1)
23                return
24            for v in parentmp[node]:
25                dfs(v, depth+1)
26
27        root = None
28        for i,v in  enumerate(parent):
29            if v == -1:
30                root = i
31        dfs(root,1)
32
33        for key,value in mp.items():
34            res += nums[key] * (maxdepth-value +1)
35
36        return res
37            