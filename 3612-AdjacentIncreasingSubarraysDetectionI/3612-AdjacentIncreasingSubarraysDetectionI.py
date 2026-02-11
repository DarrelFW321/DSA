# Last updated: 2/11/2026, 11:08:10 AM
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        startIndex = 0
        endIndex = k-1
        prev_is_increasing = False
        increasing_list_start = [0] * len(nums)
    
        while endIndex < len(nums):
            subarr = nums[startIndex:endIndex+1]
            prev = None
            is_increasing = True
            for i,v in enumerate(subarr):
                if (prev is None):
                    prev = v
                    continue
                if prev >= v:
                    is_increasing = False
                    break
                prev = v
            
            if is_increasing:
                increasing_list_start[startIndex] = 1
                if (startIndex - k >= 0):
                    if (increasing_list_start[startIndex-k] == 1):
                        return True
            
            startIndex+=1
            endIndex+=1
        return False

         
                