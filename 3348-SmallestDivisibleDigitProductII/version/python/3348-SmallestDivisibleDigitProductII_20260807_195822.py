# Last updated: 8/7/2026, 7:58:22 PM
1from functools import lru_cache
2
3class Solution:
4    def smallestNumber(self, num: str, t: int) -> str:
5        if t == 0:
6            return "-1"
7
8        # Factor t into powers of 2,3,5,7
9        powers = [0, 0, 0, 0]
10        temp = t
11
12        for i, p in enumerate((2, 3, 5, 7)):
13            while temp % p == 0:
14                temp //= p
15                powers[i] += 1
16
17        if temp != 1:
18            return "-1"
19
20        target = tuple(powers)
21
22        contrib = (
23            (0, 0, 0, 0),  # 0
24            (0, 0, 0, 0),  # 1
25            (1, 0, 0, 0),  # 2
26            (0, 1, 0, 0),  # 3
27            (2, 0, 0, 0),  # 4
28            (0, 0, 1, 0),  # 5
29            (1, 1, 0, 0),  # 6
30            (0, 0, 0, 1),  # 7
31            (3, 0, 0, 0),  # 8
32            (0, 2, 0, 0),  # 9
33        )
34
35        nums = list(map(int, num))
36        n = len(nums)
37
38        def sub(rem, val):
39            return (
40                max(0, rem[0] - val[0]),
41                max(0, rem[1] - val[1]),
42                max(0, rem[2] - val[2]),
43                max(0, rem[3] - val[3])
44            )
45
46        # Cheap necessary-condition pruning.
47        # Each digit can contribute at most:
48        # 3 factors of 2
49        # 2 factors of 3
50        # 1 factor of 5
51        # 1 factor of 7
52        def impossible(rem, slots):
53            return (
54                rem[0] > 3 * slots or
55                rem[1] > 2 * slots or
56                rem[2] > slots or
57                rem[3] > slots
58            )
59
60        # ============================================================
61        # Try answer with same length
62        # ============================================================
63
64        @lru_cache(None)
65        def can(position, remaining, greater):
66            slots = n - position
67
68            if impossible(remaining, slots):
69                return False
70
71            if position == n:
72                return remaining == (0, 0, 0, 0)
73
74            cur = nums[position]
75            start = 1 if greater else max(1, cur)
76
77            for digit in range(start, 10):
78                new_greater = greater or digit > cur
79                new_rem = sub(remaining, contrib[digit])
80
81                if can(position + 1, new_rem, new_greater):
82                    return True
83
84            return False
85
86        if can(0, target, False):
87            # Reconstruct greedily.
88            ans = []
89            pos = 0
90            rem = target
91            greater = False
92
93            while pos < n:
94                cur = nums[pos]
95                start = 1 if greater else max(1, cur)
96
97                for digit in range(start, 10):
98                    new_greater = greater or digit > cur
99                    new_rem = sub(rem, contrib[digit])
100
101                    if can(pos + 1, new_rem, new_greater):
102                        ans.append(str(digit))
103                        rem = new_rem
104                        greater = new_greater
105                        break
106
107                pos += 1
108
109            return "".join(ans)
110
111        # We don't need this cache anymore.
112        can.cache_clear()
113
114        # ============================================================
115        # Find minimum longer length
116        # ============================================================
117
118        # Start with a lower bound.
119        a, b, c, d = target
120
121        min_len = max(
122            (a + 2) // 3,
123            (b + 1) // 2,
124            c,
125            d
126        )
127
128        length = max(n + 1, min_len)
129
130        while True:
131
132            @lru_cache(None)
133            def can_long(position, remaining):
134                slots = length - position
135
136                if impossible(remaining, slots):
137                    return False
138
139                if position == length:
140                    return remaining == (0, 0, 0, 0)
141
142                for digit in range(1, 10):
143                    new_rem = sub(remaining, contrib[digit])
144
145                    if can_long(position + 1, new_rem):
146                        return True
147
148                return False
149
150            if can_long(0, target):
151                ans = []
152                rem = target
153
154                for pos in range(length):
155                    for digit in range(1, 10):
156                        new_rem = sub(rem, contrib[digit])
157
158                        if can_long(pos + 1, new_rem):
159                            ans.append(str(digit))
160                            rem = new_rem
161                            break
162
163                return "".join(ans)
164
165            can_long.cache_clear()
166            length += 1