# Last updated: 2/11/2026, 11:08:12 AM
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        currExchange = numExchange

        fullBottles = numBottles
        emptyBottles = 0
        total = 0

        while (fullBottles > 0):
            #DRINK THE FULL
            total += fullBottles

            #EMPTY BOTTLES
            emptyBottles += fullBottles
            fullBottles = 0


            #Exchange
            while (emptyBottles >= currExchange):
                emptyBottles-=currExchange
                fullBottles+=1
                currExchange+=1
            
        return total