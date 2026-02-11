# Last updated: 2/11/2026, 11:08:14 AM
class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """


        mp = {}
        res = []

        for i,v in enumerate(nums):
            mp[v] = mp.get(v,0) +1

        for key,value in mp.items():
            if value > 1:
                res.append(key)
        
        return res
        