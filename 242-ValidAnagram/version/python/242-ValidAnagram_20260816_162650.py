# Last updated: 8/16/2026, 4:26:50 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        s_map = defaultdict(int)
4        t_map = defaultdict(int)
5
6        for i,v in enumerate(s):
7            s_map[v]+=1
8
9        for i,v in enumerate(t):
10            t_map[v]+=1
11
12        if s_map == t_map:
13            return True
14        else:
15            return False
16