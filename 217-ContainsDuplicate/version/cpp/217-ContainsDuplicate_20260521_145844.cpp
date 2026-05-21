// Last updated: 5/21/2026, 2:58:44 PM
1#include <unordered_map>
2using namespace std;
3
4
5class Solution {
6public:
7    bool containsDuplicate(vector<int>& nums) {
8        unordered_set<int> st;
9        for (auto i :nums){
10            if (st.count(i) == 1){
11                return true;
12            }
13            st.insert(i);
14
15        }
16        return false;
17    }
18};