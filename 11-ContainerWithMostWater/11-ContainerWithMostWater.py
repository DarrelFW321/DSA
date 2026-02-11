# Last updated: 2/11/2026, 11:08:50 AM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxarea = 0

        if(len(height) == 0):
            return 0

        while (left < right):
            area = (right - left) * min (height[right],height[left])
            if (height[right] > height[left]):
                left+=1
            else:
                right-=1
            maxarea = max(area, maxarea)

        return maxarea