// Last updated: 5/21/2026, 3:32:51 PM
1class Solution {
2public:
3    vector<int> twoSum(vector<int>& nums, int target) {
4        unordered_map<int,int> mp;
5        
6        for (int i = 0; i < nums.size(); i++){
7            int needed = target - nums[i];
8            if (mp.count(needed) ==1){
9                return vector<int>{i, mp[needed]};
10            }
11            mp[nums[i]] = i;
12        }
13        return vector<int>{0,1};
14    }
15};