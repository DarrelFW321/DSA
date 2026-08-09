# Last updated: 8/9/2026, 12:39:02 AM
1class Solution:
2    def maxArea(self, mat: List[List[int]]) -> int:
3        m = len(mat)
4        n = len(mat[0])
5
6        valmerinto = mat
7
8        # 2D prefix sum
9        prefix = [[0] * (n + 1) for _ in range(m + 1)]
10
11        for i in range(m):
12            for j in range(n):
13                prefix[i + 1][j + 1] = (
14                    prefix[i][j + 1]
15                    + prefix[i + 1][j]
16                    - prefix[i][j]
17                    + mat[i][j]
18                )
19
20        # check whether square starting at (i,j)
21        # with side length k is entirely 1s
22        def valid_square(i, j, k):
23            total = (
24                prefix[i + k][j + k]
25                - prefix[i][j + k]
26                - prefix[i + k][j]
27                + prefix[i][j]
28            )
29
30            return total == k * k
31
32        # Check whether TWO non-overlapping k x k squares exist
33        def can_make(k):
34            min_row = m
35            max_row = -1
36            min_col = n
37            max_col = -1
38
39            count = 0
40
41            for i in range(m - k + 1):
42                for j in range(n - k + 1):
43
44                    if not valid_square(i, j, k):
45                        continue
46
47                    count += 1
48
49                    min_row = min(min_row, i)
50                    max_row = max(max_row, i)
51
52                    min_col = min(min_col, j)
53                    max_col = max(max_col, j)
54
55                    if count >= 2:
56                        # separated vertically
57                        if max_row - min_row >= k:
58                            return True
59
60                        # separated horizontally
61                        if max_col - min_col >= k:
62                            return True
63
64            return False
65
66        lo = 1
67        hi = min(m, n)
68        best = 0
69
70        while lo <= hi:
71            mid = (lo + hi) // 2
72
73            if can_make(mid):
74                best = mid
75                lo = mid + 1
76            else:
77                hi = mid - 1
78
79        return best * best