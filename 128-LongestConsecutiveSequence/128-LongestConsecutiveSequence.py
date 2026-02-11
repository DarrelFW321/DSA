# Last updated: 2/11/2026, 11:08:34 AM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        res = 0

        for num in st:
            if (num-1 not in st):
                leng = 1
                while (num + leng in st):
                    leng+=1
                res = max (res, leng)
        return res