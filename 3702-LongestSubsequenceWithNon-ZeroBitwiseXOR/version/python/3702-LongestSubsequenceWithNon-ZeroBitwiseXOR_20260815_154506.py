# Last updated: 8/15/2026, 3:45:06 PM
1class Solution:
2    def longestSubsequence(self, nums: List[int]) -> int:
3        xor_all = 0
4
5        for num in nums:
6            xor_all ^= num
7
8        # Entire array already has non-zero XOR
9        if xor_all != 0:
10            return len(nums)
11
12        # XOR of entire array is 0.
13        # If there's a non-zero number x, remove it.
14        # New XOR = xor_all ^ x = 0 ^ x = x != 0
15        for num in nums:
16            if num != 0:
17                return len(nums) - 1
18
19        # Every number is 0, so every subsequence has XOR 0
20        return 0