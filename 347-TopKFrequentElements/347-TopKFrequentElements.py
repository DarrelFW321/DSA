# Last updated: 2/11/2026, 11:08:24 AM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}

        for num in nums:
            mp[num] = mp.get(num,0) + 1
            
        buckets = [[] for _ in range(len(nums)+1)]
        
        for key,value in mp.items():
            buckets[value].append(key)
            
        res = []
        current_count = 0
            
        for i in range(len(nums),0,-1):
            for key in buckets[i]:
                if (current_count < k):
                    current_count+=1
                    res.append(key)
        
        return res



        