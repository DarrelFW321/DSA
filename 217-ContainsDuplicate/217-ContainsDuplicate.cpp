// Last updated: 2/11/2026, 11:08:26 AM
#include <set>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> st;

        for (int i = 0; i< size(nums); ++i){
            if (st.find(nums[i]) != st.end()){
                return true;
            }
            else{
                st.insert(nums[i]);
            }
        }
        return false;
        
    }
};