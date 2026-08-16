# Last updated: 8/16/2026, 4:09:13 PM
1class Solution(object):
2    def containsDuplicate(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: bool
6        """
7        st = set()
8
9        for i,v in enumerate(nums):
10            if v in st:
11                return True
12            st.add(v)
13
14
15        return False