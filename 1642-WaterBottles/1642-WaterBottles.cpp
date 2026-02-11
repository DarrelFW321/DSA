// Last updated: 2/11/2026, 11:08:18 AM
class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int fullBottles = numBottles;
        int emptyBottles = 0;
        int total = 0;

        while (fullBottles > 0){
            total += fullBottles;

            emptyBottles += fullBottles;

            fullBottles = emptyBottles/numExchange;
            emptyBottles = emptyBottles%numExchange;
        }

        return total;
    }
};