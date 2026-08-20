# Last updated: 8/20/2026, 7:50:51 PM
1class Solution:
2    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
3        rows = defaultdict(set)
4        
5        for row,seat in reservedSeats:
6            rows[row].add(seat)
7        
8        # print(st)
9
10        res = (n - len(rows)) * 2
11
12        for row,seats in rows.items():
13
14            leftblock = True
15            rightblock = True
16            midblock = True
17            
18            
19            if 4 in seats or 5 in seats:
20                leftblock = False
21                midblock = False
22
23            if 6 in seats or 7 in seats:
24                rightblock = False
25                midblock = False
26
27            if leftblock:
28                if 2 in seats or 3 in seats:
29                    leftblock = False
30
31            if rightblock:
32                if 8 in seats or 9 in seats:
33                    rightblock = False
34
35            if leftblock and rightblock:
36                res += 2
37            elif leftblock or rightblock or midblock:
38                res += 1
39            
40
41            # print ("leftblock ", leftblock)
42            # print ("rightblock ", rightblock)
43            # print ("midblock ", midblock)
44            # print("res ", res)
45
46        return res
47
48