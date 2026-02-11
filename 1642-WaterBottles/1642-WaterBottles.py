# Last updated: 2/11/2026, 11:08:21 AM
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        fullBottles = numBottles
        emptyBottles = 0

        total = 0
        
        while (fullBottles > 0):
            #drink the full bottles
            total+= fullBottles
            
            #now the dranked fullbottles are empty bottles

            emptyBottles += fullBottles

            #exchange emptybottles for fullbottles
            fullBottles = emptyBottles//numExchange
            #they may be some empty bottle remain
            emptyBottles = emptyBottles%numExchange


        return total

        