// Last updated: 2/11/2026, 11:08:17 AM
#include <vector>
using namespace std;

class Solution {
public:
    int totalMoney(int n) {
        vector<int> arr {0,1,2,3,4,5,6};
        int index =0;
        int res = 0;

        for (int i =0 ; i< n; ++i){
            if (index > 6){
                index = 0;
            }

            arr.at(index)++;
            res+= arr.at(index);
            index++;

        }
        return res;
    }

};