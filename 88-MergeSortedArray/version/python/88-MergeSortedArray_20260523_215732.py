# Last updated: 5/23/2026, 9:57:32 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6
7        temp = nums1[:m]
8
9        i = 0
10        j = 0
11        while (i < m and j < n):
12            if (temp[i] <= nums2[j]):
13                nums1[i+j] = temp[i]
14                i+=1
15            else:
16                nums1[i+j] = nums2[j]
17                j+=1
18
19        while (i < m):
20            nums1[i+j] = temp[i]
21            print (" i + j ", i+j)
22            print ("temp[i] ", temp[i])
23            i+=1
24
25        while (j < n):
26            nums1[i+j] = nums2[j]
27            print (" i + j ", i+j)
28            print ("nums2[j] ", nums2[j])
29            j+=1
30    