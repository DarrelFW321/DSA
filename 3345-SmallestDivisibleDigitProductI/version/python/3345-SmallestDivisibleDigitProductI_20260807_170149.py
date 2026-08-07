# Last updated: 8/7/2026, 5:01:49 PM
1class Solution:
2    def smallestNumber(self, n: int, t: int) -> int:
3        res = n
4        while (True):
5            digits  = []
6            temp = res
7            while temp > 0:
8                digit = temp % 10
9                digits.append(digit)
10                temp = temp//10
11
12            product = 1
13            for digit in digits:
14                product = product * digit
15            
16            if product % t == 0:
17                return res
18            else:
19                res+=1