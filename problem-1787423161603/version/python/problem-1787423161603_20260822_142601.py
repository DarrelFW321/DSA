# Last updated: 8/22/2026, 2:26:01 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        res  = ""
4        for char in s:
5            if char.isalnum():
6                res+=char.lower()
7        
8        # print(res)
9
10        l = 0
11        r = len(res)-1
12
13        while (l < r):
14            if res[l] != res[r]:
15                return False
16            l+=1
17            r-=1
18        
19        return True