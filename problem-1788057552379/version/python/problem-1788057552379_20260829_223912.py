# Last updated: 8/29/2026, 10:39:12 PM
1class Solution:
2    def countSpecialIntegers(self, nums: list[int]) -> int:
3        mp = defaultdict(int)
4        st = set()
5
6        for i,v in enumerate(nums):
7            if v in mp:
8                if mp[v] == i-1:
9                    mp[v] = i
10                else:
11                    if v in st:
12                        st.remove(v)
13
14            else:
15                mp[v] = i
16                st.add(v)
17            print(mp)
18            print(st)
19
20        return len(st)
21            
22                