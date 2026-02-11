# Last updated: 2/11/2026, 11:08:35 AM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}


        for i,str in enumerate(strs):
            arr = [0]*26
            for ch in str:
                arr[ord(ch)-ord("a")] +=1
            if tuple(arr) not in mp:
                mp[tuple(arr)] = []
            mp[tuple(arr)].append(str)

        res = []

        for key,value in mp.items():
            res.append(value)

        return res

            