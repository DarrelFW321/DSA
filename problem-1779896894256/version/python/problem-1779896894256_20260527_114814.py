# Last updated: 5/27/2026, 11:48:14 AM
1class Solution:
2    def passwordStrength(self, password: str) -> int:
3        res = 0
4        tracker = set()
5        
6
7        for char in password:
8            if char in tracker:
9                continue
10            if char >= 'a' and char <= 'z':
11                res+=1
12                tracker.add(char)
13            elif char >= 'A' and char <= 'Z':
14                res+=2
15                tracker.add(char)
16            elif char >= '0' and char <= '9':
17                res+=3
18                tracker.add(char)
19            elif char in ["!","@","#","$"]:
20                res+=5
21                tracker.add(char)
22
23        return res