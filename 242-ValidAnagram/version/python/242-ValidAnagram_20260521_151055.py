# Last updated: 5/21/2026, 3:10:55 PM
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        s_map = {}
4        t_map = {}
5
6        for ch in s:
7            s_map[ch] = s_map.get(ch,0) +1
8
9        for ch in t:
10            t_map[ch] = t_map.get(ch,0) + 1
11
12        if (s_map == t_map):
13            return True
14
15        return False
16