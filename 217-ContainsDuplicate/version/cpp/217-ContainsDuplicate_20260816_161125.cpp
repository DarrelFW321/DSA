// Last updated: 8/16/2026, 4:11:25 PM
1
2class Solution {
3public:
4    bool containsDuplicate(vector<int>& nums) {
5        unordered_set<int> st{};
6        
7        for (auto i : nums){
8            if (st.contains(i)) return true;
9            st.insert(i);
10        }
11
12        return false;
13
14    }
15};