# Last updated: 8/13/2026, 1:55:19 AM
1class Solution:
2    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
3        segmentree = [None] * 4*len(s)
4        n = len(s)
5        chars = list(s)
6
7        def merge(L, R):
8            lc, lr, lp, ls, lb, llen = L
9            rc, rr, rp, rs, rb, rlen = R
10
11            prefix = lp
12            suffix = rs
13            best = max(lb, rb)
14
15            if lr == rc:
16                best = max(best, ls + rp)
17
18                if lp == llen:
19                    prefix = llen + rp
20
21                if rs == rlen:
22                    suffix = rlen + ls
23
24            return [lc, rr, prefix, suffix, best, llen + rlen]
25
26            
27
28        def buildtree(v, tl,tr):
29            if tl == tr:
30                c = chars[tl]
31                segmentree[v] = [c, c, 1, 1, 1, 1]
32                return
33
34            else:
35                tm = (tl + tr)//2
36                buildtree(v*2, tl,tm)
37                buildtree(v*2 + 1, tm+1,tr)
38                segmentree[v] = merge(
39                    segmentree[v * 2],
40                    segmentree[v * 2 + 1]
41                )
42                ...
43
44        def update(v, tl, tr, pos, newstuff):
45            if tl == tr:
46                segmentree[v] = [newstuff, newstuff, 1, 1, 1, 1]
47                return
48            else:
49                tm = (tl+tr)//2
50                if pos <= tm:
51                    update(v*2, tl, tm, pos, newstuff)
52                else:
53                    update(v*2 + 1, tm+1, tr ,pos, newstuff)
54            segmentree[v] = merge(
55                segmentree[v * 2],
56                segmentree[v * 2 + 1]
57            )
58
59        buildtree(1, 0, len(s) - 1)
60
61        ans = []
62
63        for pos, c in zip(queryIndices, queryCharacters):
64            update(1, 0, n - 1, pos, c)
65            ans.append(segmentree[1][4])
66
67        return ans
68
69