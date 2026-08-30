# Last updated: 8/30/2026, 7:03:15 PM
1class Solution:
2    def sumDecoded(self, nums: list[int]) -> int:
3        res = 0
4        MOD = (10 ** 9) + 7
5
6        def split(val, first):
7            temp = str(val)
8            x = temp[:first]
9            y = temp[first:]
10            return int(x),int(y)
11            
12
13        for i,v in enumerate(nums):
14            width  = v % 10
15            d = floor(v/10)
16            x,y = split(d,width)
17
18            res = (res  + pow(x,y,MOD)) % MOD
19
20        return res
21            
22            