# Last updated: 2/11/2026, 11:08:28 AM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]* len(nums)
        right = [1] * len(nums)

        leftproduct = 1
        for i in range(len(nums)):
            left[i] = leftproduct
            leftproduct *= nums[i]

        rightproduct = 1
        for i in range(len(nums)-1, -1,-1):
            right[i] = rightproduct
            rightproduct *= nums[i]

        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = left[i] * right[i]

        return res
