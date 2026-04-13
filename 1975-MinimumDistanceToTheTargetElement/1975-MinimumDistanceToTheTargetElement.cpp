// Last updated: 4/13/2026, 12:49:11 PM
class Solution {
public:
    int getMinDistance(vector<int>& nums, int target, int start) {
        vector<int> possible;
        for (int i = 0; i < nums.size(); i++){
            if (nums[i]==target){
                possible.push_back(i);
            }
        }
        int min = INT_MAX;
        for (auto i : possible){
            int diff = i - start;
            if (diff < 0){
                diff = -diff;
            }
            if (diff < min){
                min = diff;
            }
        }
        return min;
    }
};