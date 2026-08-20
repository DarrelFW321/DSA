# Last updated: 8/20/2026, 7:13:38 PM
1class Solution:
2    def resultArray(self, nums: List[int]) -> List[int]:
3        # print(nums)
4
5        # res = []
6        arr1 = []
7        arr2 = []
8
9        if len(nums) <=2:
10            return  nums
11
12
13        arr1.append(nums[0])
14        arr2.append(nums[1])
15
16        for i in range(2, len(nums)):
17            if arr1[len(arr1)-1] > arr2[len(arr2)-1]:
18                arr1.append(nums[i])
19            else:
20                arr2.append(nums[i])
21
22        return arr1 + arr2
23