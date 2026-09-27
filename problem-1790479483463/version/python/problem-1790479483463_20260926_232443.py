# Last updated: 9/26/2026, 11:24:43 PM
1class Solution:
2    def rearrangeArray(self, nums: list[int]) -> list[int]:
3        mp = defaultdict(int)
4
5        ans = []
6
7        for i,v in enumerate (nums):
8            mp[v]+=1
9
10        while mp:
11            temp = []
12            to_delete = []
13            for key,val in mp.items():
14                mp[key]-=1
15                if mp[key] == 0:
16                    to_delete.append(key)
17                temp.append(key)
18            for key in to_delete:
19                mp.pop(key)
20            temp.sort()
21            ans+=temp
22
23        return ans
24
25        