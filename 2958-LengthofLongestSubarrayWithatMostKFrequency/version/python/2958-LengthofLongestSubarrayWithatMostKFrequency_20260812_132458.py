# Last updated: 8/12/2026, 1:24:58 PM
1class Solution:
2    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
3        mp = defaultdict(int)
4        left = 0
5        right = 0
6        res = 0
7        
8        if (len(nums)) == 0:
9            return 0
10
11        while (right >= left and right < len(nums)):
12            # print("left : ", left)
13            # print("right: ", right)
14            i = nums[right]
15            mp[i]+=1
16            while (mp[i] > k):
17                mp[nums[left]]-=1
18                left +=1
19            res = max(res,(right - left + 1))
20            # print("res :", res)
21            right +=1
22
23        return res
24