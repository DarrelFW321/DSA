// Last updated: 2/11/2026, 11:08:55 AM
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> mp;

        for (int i =0; i< size(nums); ++i){
            if(mp.find(target-nums[i])!= mp.end()){
                return {i, mp[target-nums[i]]};
            }
            mp[nums[i]] = i;
        }
        return {};
    }
};