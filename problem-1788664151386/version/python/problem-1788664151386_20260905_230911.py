# Last updated: 9/5/2026, 11:09:11 PM
1class Solution:
2    def countRotations(self, s: str, k: int) -> int:
3        mp = defaultdict(int)
4
5        for i in range(len(s)):
6            new = s[i:] + s[0:i]
7            
8            score = 0
9            for j in range(len(s)-1):
10                if new[j] == new[j+1]:
11                    score+=1
12            # print(new)
13            # print(score)
14
15            mp[score]+=1
16
17        return mp[k]