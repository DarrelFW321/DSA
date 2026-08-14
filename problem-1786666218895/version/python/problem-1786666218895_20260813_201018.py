# Last updated: 8/13/2026, 8:10:18 PM
1class Solution:
2    def maximumLengthSubstring(self, s: str) -> int:
3        best = 0
4        if len(s) == 0:
5            return 0
6
7        mp = defaultdict(int)
8
9        l = 0
10        r = 0
11
12        while (l <= r and r < len(s)):
13            mp[s[r]]+=1
14
15            while mp[s[r]] > 2:
16                mp[s[l]] -=1
17                l +=1
18
19            r+=1
20            best = max(best,r-l)
21
22        return best
23