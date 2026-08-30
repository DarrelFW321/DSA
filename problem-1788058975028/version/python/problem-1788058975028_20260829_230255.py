# Last updated: 8/29/2026, 11:02:55 PM
1class Solution:
2    def sumDecoded(self, nums: list[int]) -> int:
3        res = 0
4
5        def getxy(di, widthi):
6            digits = []
7
8            temp = di
9            while temp>0:
10                dig = temp%10 
11                digits.append(dig)
12                temp = temp//10
13
14            leny = len(digits)-widthi
15            y = 0
16            x = 0
17            coefficient = 1
18            for i in range(0,leny):
19                y += digits[i] * coefficient
20                coefficient*=10
21
22            coefficient = 1
23            for i in range(leny,len(digits)):
24                x += digits[i] * coefficient
25                coefficient*=10
26
27            return x,y
28
29        mod = 10 ** 9 + 7
30        for i,v in enumerate(nums):
31            widthi = v % 10
32            di = floor(v/10)
33
34            x,y = getxy(di,widthi)
35            # print(x,y)
36            res= (res + pow(x,y,mod)) % mod
37
38        return res
39            