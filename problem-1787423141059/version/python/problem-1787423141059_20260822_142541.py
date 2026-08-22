# Last updated: 8/22/2026, 2:25:41 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        s = s.strip()
4        res  = ""
5        for char in s:
6            if char.isalnum():
7                res+=char.lower()
8        
9        print(res)
10
11        l = 0
12        r = len(res)-1
13
14        while (l < r):
15            if res[l] != res[r]:
16                return False
17            l+=1
18            r-=1
19        
20        return True