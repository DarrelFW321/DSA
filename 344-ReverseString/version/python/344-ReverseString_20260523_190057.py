# Last updated: 5/23/2026, 7:00:57 PM
1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        """
4        Do not return anything, modify s in-place instead.
5        """
6        for i,v in enumerate (s):
7            if (len(s)-i-1 <= i):
8                break
9            temp = s[len(s) -i-1]
10            s[len(s)-i-1] = v
11            s[i] = temp
12
13        
14        
15
16        