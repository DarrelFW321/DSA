# Last updated: 8/20/2026, 8:15:49 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3
4        freq = defaultdict(int)
5
6        for num in nums:
7            freq[num]+=1
8        
9        heap = []
10
11        for num,count in freq.items():
12            heapq.heappush(heap,(count,num))
13            if len(heap) > k:
14                heapq.heappop(heap)
15
16        res = []
17        for val in heap:
18            res.append(val[1])
19        return res
20        
21