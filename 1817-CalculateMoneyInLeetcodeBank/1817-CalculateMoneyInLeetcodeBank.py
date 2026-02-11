# Last updated: 2/11/2026, 11:08:19 AM
class Solution:
    def totalMoney(self, n: int) -> int:
        arr = [0,1,2,3,4,5,6]
        res = 0
        index = 0

        for i in range(n):
            if (index >6):
                index = 0
            arr[index]+=1
            res+=arr[index]
            index+=1

        return res

        