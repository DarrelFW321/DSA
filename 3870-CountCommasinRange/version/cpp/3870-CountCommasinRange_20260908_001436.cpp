// Last updated: 9/8/2026, 12:14:36 AM
1class Solution {
2public:
3    int countCommas(int n) {
4        long long ans = 0;
5
6        for (long long x = 1000; x <= n; ) {
7            ans += n - x + 1;
8
9            // Prevent overflow
10            if (x > n / 1000)
11                break;
12
13            x *= 1000;
14        }
15
16        return ans;
17    }
18};