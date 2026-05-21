# Last updated: 5/21/2026, 2:52:25 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        st = set()
4
5        for i in nums:
6            if i in st:
7                return True
8            st.add(i)
9
10        return False