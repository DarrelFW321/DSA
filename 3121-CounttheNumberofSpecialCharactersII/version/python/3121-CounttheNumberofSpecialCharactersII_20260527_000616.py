# Last updated: 5/27/2026, 12:06:16 AM
1class Solution:
2    def numberOfSpecialChars(self, word: str) -> int:
3        mp = {}
4        res = 0
5
6        for i,v in enumerate(word):
7            if v.lower() not in mp:
8                mp[v.lower()] = [False,False,None]
9            
10            if (v == v.lower()):
11                if mp[v.lower()][1]:
12                    mp[v.lower()][2] = False
13                mp[v.lower()][0] = True
14            else:
15                if mp[v.lower()][0] and mp[v.lower()][2] is None:
16                    mp[v.lower()][2] = True
17                elif not mp[v.lower()[0]]:
18                    mp[v.lower()][2] = False
19
20                mp[v.lower()][1] = True
21        print(mp)
22        for key,value in mp.items():
23            if (value[0] and value[1] and value[2]):
24                res+=1
25
26        return res