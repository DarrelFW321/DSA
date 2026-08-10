# Last updated: 8/9/2026, 10:08:12 PM
1class Solution:
2    def winnerSquareGame(self, n: int) -> bool:
3        
4        mp = {}
5
6        def dp(num):
7            if num in mp:
8                return mp[num]
9            if num == 0:
10                mp[num] = False
11                return False
12
13            for i in range(1, num+1):
14                if i*i > num:
15                    break
16                if not dp(num-(i*i)):
17                    mp[num] = True
18                    return True
19
20            mp[num] = False
21            return False
22
23        return dp(n)
24
25
26            