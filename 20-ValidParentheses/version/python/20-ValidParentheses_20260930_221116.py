# Last updated: 9/30/2026, 10:11:16 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        left = {"{" : "}", "(": ")", "[" : "]"}
5
6
7        for char in s:
8            if char in left:
9                stack.append(char)
10            elif char in left.values():
11                if stack and left[stack[-1]] == char:
12                    stack.pop()
13                else:
14                    return False
15
16        return len(stack) == 0
17
18            