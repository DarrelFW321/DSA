# Last updated: 8/22/2026, 12:35:39 PM
1class Solution:
2    def checkDivisibility(self, n: int) -> bool:
3        sumdig = 0
4        product = 1
5
6        temp = n
7
8        while (temp > 0):
9            dig = temp%10
10            temp= temp//10
11
12            sumdig+=dig
13            product*=dig
14
15        # print(sumdig)
16        # print(product)
17        if (n%(sumdig + product) == 0):
18            return True
19        else:
20            return False