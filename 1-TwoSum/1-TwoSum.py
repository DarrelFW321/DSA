# Last updated: 2/11/2026, 11:08:56 AM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        mp = {}

        for i,num in enumerate(nums):
            if target-num in mp:
                return [mp[target-num],i]
            mp[num] = i


        