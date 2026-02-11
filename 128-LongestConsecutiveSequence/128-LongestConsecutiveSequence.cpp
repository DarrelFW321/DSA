// Last updated: 2/11/2026, 11:08:32 AM
#include <unordered_set>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> st;
        for (int i : nums){
            st.insert(i);
        }


        int res = 0;
        for (int i : st){
            if (st.find(i-1) == st.end()){
                int length = 1;

                while (st.find(i+length) != st.end()){
                    length++;
                }

                if (length > res){
                    res = length;
                }


            }
        }
        return res;
    }
};