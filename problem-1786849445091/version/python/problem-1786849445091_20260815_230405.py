# Last updated: 8/15/2026, 11:04:05 PM
1class Solution:
2    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
3
4        longest = max(lights)
5
6        res = 0
7
8        for i,v in enumerate(arrivalTime):
9            r = v % period
10            if r < longest:
11                continue
12            else:
13                res = max(res,period-r)
14
15        return res
16
17                    
18            
19            
20            