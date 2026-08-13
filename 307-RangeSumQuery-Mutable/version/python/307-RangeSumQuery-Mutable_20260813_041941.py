# Last updated: 8/13/2026, 4:19:41 AM
1class NumArray:
2
3    def __init__(self, nums: List[int]):
4        self.n = len(nums)
5        self.tree = [0] * (4 * self.n)
6
7        def build(v, tl, tr):
8            if tl == tr:
9                self.tree[v] = nums[tl]
10                return
11
12            tm = (tl + tr) // 2
13
14            build(v * 2, tl, tm)
15            build(v * 2 + 1, tm + 1, tr)
16
17            self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]
18
19        build(1, 0, self.n - 1)
20
21    def update(self, index: int, val: int) -> None:
22
23        def update_tree(v, tl, tr):
24            if tl == tr:
25                self.tree[v] = val
26                return
27
28            tm = (tl + tr) // 2
29
30            if index <= tm:
31                update_tree(v * 2, tl, tm)
32            else:
33                update_tree(v * 2 + 1, tm + 1, tr)
34
35            self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]
36
37        update_tree(1, 0, self.n - 1)
38
39    def sumRange(self, left: int, right: int) -> int:
40
41        def query(v, tl, tr, l, r):
42            if l > r:
43                return 0
44
45            if l == tl and r == tr:
46                return self.tree[v]
47
48            tm = (tl + tr) // 2
49
50            return (
51                query(v * 2, tl, tm, l, min(r, tm))
52                +
53                query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r)
54            )
55
56        return query(1, 0, self.n - 1, left, right)
57        
58
59
60# Your NumArray object will be instantiated and called as such:
61# obj = NumArray(nums)
62# obj.update(index,val)
63# param_2 = obj.sumRange(left,right)