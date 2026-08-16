# Last updated: 8/15/2026, 11:26:44 PM
1class Solution:
2    def maximumGap(self, skill: str, station: str) -> int:
3
4
5        if len(skill) == 1:
6            return 0
7        left= []
8        right = [0] * len(skill)
9
10        curr = 0
11        for i in  range(len(station)) :
12            if curr >= len(skill):
13                break
14            if station[i] == skill[curr]:
15                left.append(i)
16                curr+=1
17
18        curr = len(skill)-1
19        for i in  range(len(station)-1, -1,-1) :
20            if curr < 0:
21                break
22            if station[i] == skill[curr]:
23                right[curr] = i
24                curr-=1
25
26        # print(left)
27        # print(right)
28        res = 0
29        for j in range(len(skill)-1):
30            gap = right[j+1]-left[j]
31            res = max(res,gap)
32
33        return res
34
35        
36            