# Last updated: 2/11/2026, 11:08:44 AM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        
        for idx,num in  enumerate(nums):
            if (idx>0 and num == nums[idx-1]):
                continue
    
            target = -num
            left = idx+1
            right = len(nums)-1
            while (left < right):
                if nums[left] + nums[right] == target:
                    res.append([num, nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left+=1
                else:
                    right-=1
    

        return res