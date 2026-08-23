# Last updated: 8/22/2026, 11:12:04 PM
1class Solution:
2    def isPalindromic(self, s: str) -> bool:
3
4        def convertbinary(i):
5            if i ==0:
6                return "0"
7            res = ""
8            temp = i
9            while temp >0:
10                res+= str(temp % 2)
11                temp = temp//2
12
13 
14
15            res = res[::-1]
16
17            while len(res) < 8:
18                res = "0" + res
19
20            return res
21
22        temp = ""
23        for ch in s:
24            temp+=convertbinary(ord(ch))
25
26        for i in range(len(temp)):
27            if temp[i] != temp[len(temp)-i-1]:
28                return False
29        return True