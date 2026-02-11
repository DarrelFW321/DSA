// Last updated: 2/11/2026, 11:08:22 AM
#include <unordered_map>
#include <vector>

using namespace std;


class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        
        for (auto i: nums){
            mp[i]++;
        }

        vector<vector<int>> arr (nums.size()+1);

        for (auto &[key, value]: mp){
            arr[value].push_back(key);
        }

        vector<int>res;
        int count = 0;

        for (int i = nums.size(); count < k && i >= 0; --i){
            for (auto v: arr[i]){
                count++;
                res.push_back(v);
            }
        }

        return res;

    }
};