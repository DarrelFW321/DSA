# Last updated: 8/15/2026, 9:25:09 PM
1class Solution:
2    def stoneGameIX(self, stones: List[int]) -> bool:
3        
4        
5        # arr = [i for i in range(len(stones))]
6
7        # def dp(sum, remainingindex, aliceturn):
8        #     if not remainingindex:
9        #         return not aliceturn
10
11        #     for i,v in  enumerate(remainingindex):
12        #         temp = sum + stones[v]
13        #         if temp % 3 == 0:
14        #             continue
15        #         temparr = remainingindex[0:i] + remainingindex[i+1:]
16        #         if not dp(temp, temparr, not aliceturn):
17        #             return True
18
19        #     return False
20
21        # return dp(0,arr, True)
22
23        # cnt = [0]*3
24
25
26        # for x in stones:
27        #     cnt[x % 3] += 1
28
29        # @lru_cache(None)
30        # def dp (mod, c0,c1,c2,aliceturn):
31        #     if c0+c1+c2 == 0:
32        #         return not aliceturn
33
34        #     counts = [c0,c1,c2]
35        #     for r in range(3):
36        #         if counts[r] == 0:
37        #             continue
38
39        #         newmod = (mod+r) % 3
40
41        #         if newmod==0:
42        #             continue
43
44        #         newcounts = counts[:]
45        #         newcounts[r] -= 1
46
47        #         if not dp(
48        #             newmod,
49        #             newcounts[0],
50        #             newcounts[1],
51        #             newcounts[2],
52        #             not aliceturn
53        #         ):
54        #             return True
55
56        #     return False
57
58        # return dp(0, cnt[0], cnt[1], cnt[2], True)
59
60
61        cnt = [0, 0, 0]
62
63        for x in stones:
64            cnt[x % 3] += 1
65
66        c0, c1, c2 = cnt
67
68        if c0 % 2 == 0:
69            return c1 > 0 and c2 > 0
70        else:
71            return abs(c1 - c2) > 2