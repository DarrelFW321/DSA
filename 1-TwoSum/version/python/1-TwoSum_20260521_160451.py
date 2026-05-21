# Last updated: 5/21/2026, 4:04:51 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        mp = {} #sorted string -> list of strings
4
5        for word in strs:
6            key = "".join(sorted(word))
7            if key in mp:
8                mp[key].append(word)
9            else:
10                mp[key]  =[word]
11        
12        res =[]
13        for key,arr in mp.items():
14            res.append(arr)
15
16        return res
17
18