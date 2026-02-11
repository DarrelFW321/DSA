# Last updated: 2/11/2026, 11:08:11 AM
class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # n >= 3 assumed by the problem
        if n == 3:
            return nums[0] + nums[1] + nums[2]

        min_i = nums[1]              # best nums[i] so far, i starts at 1
        best_pair_sum = float('inf') # best nums[i] + nums[j]

        for j in range(2, n):        # j can go up to n-1
            best_pair_sum = min(best_pair_sum, min_i + nums[j])
            min_i = min(min_i, nums[j])  # nums[j] becomes a candidate i for future j's

        return nums[0] + best_pair_sum
        