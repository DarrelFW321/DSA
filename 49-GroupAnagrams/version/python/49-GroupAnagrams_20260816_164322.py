# Last updated: 8/16/2026, 4:43:22 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        
4
5        mp = defaultdict(list)
6
7        for i,v in enumerate(strs):
8            arr = [0] * 26
9            for char in v:
10                arr[ord(char)-97]+=1
11
12            hashindex = tuple(arr)
13            mp[hashindex].append(v)
14
15        res = []
16        for i in mp.values():
17            res.append(i)
18
19        return res
20
21
22            