# Last updated: 5/27/2026, 12:07:49 AM
1class Solution:
2    def numberOfSpecialChars(self, word: str) -> int:
3        last_lower = {}
4        first_upper = {}
5
6        for i, ch in enumerate(word):
7            lower = ch.lower()
8
9            if ch.islower():
10                last_lower[lower] = i
11            else:
12                if lower not in first_upper:
13                    first_upper[lower] = i
14
15        res = 0
16        for ch in last_lower:
17            if ch in first_upper and last_lower[ch] < first_upper[ch]:
18                res += 1
19
20        return res