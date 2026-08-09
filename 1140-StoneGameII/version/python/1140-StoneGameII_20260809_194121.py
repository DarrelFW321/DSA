# Last updated: 8/9/2026, 7:41:21 PM
1class Solution:
2    def stoneGameII(self, piles: List[int]) -> int:
3        n = len(piles)
4
5        # suffix[i] = total stones from piles[i] to the end
6        suffix = [0] * (n + 1)
7        for i in range(n - 1, -1, -1):
8            suffix[i] = suffix[i + 1] + piles[i]
9
10        @lru_cache(None)
11        def dp(i, M):
12            # Can take every remaining pile
13            if i + 2 * M >= n:
14                return suffix[i]
15
16            best = 0
17
18            for X in range(1, 2 * M + 1):
19                opponent = dp(i + X, max(M, X))
20                current = suffix[i] - opponent
21                best = max(best, current)
22
23            return best
24
25        return dp(0, 1)