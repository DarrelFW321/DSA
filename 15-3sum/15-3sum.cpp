// Last updated: 2/11/2026, 11:08:42 AM
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(),nums.end());


        for (int i = 0; i < nums.size(); ++i){
            if (i > 0 and nums[i] == nums[i-1]){
                continue;
            }
            int v = nums[i];
            int left = i+1;
            int right = nums.size()-1;

            while (left < right){
                int total = v + nums[left] + nums[right];
                if (total == 0){
                    res.push_back(vector<int>{v,nums[left],nums[right]});

                    left++;
                    right--;

                    while (left < right && nums[left] == nums[left-1]){
                        left++;
                    }

                    while (left < right && nums[right] == nums[right+1]){
                        right--;
                    }
                }

                else if (total > 0){
                    right--;
                }
                else left++;

            }
        }
        return res;
    }

};