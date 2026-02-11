# Last updated: 2/11/2026, 11:08:29 AM
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        st = set()
        for num in nums:
            if num in st:
                return True
            st.add(num)
        
        return False
        