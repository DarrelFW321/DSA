// Last updated: 2/11/2026, 11:08:24 AM
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int>left (nums.size(), 1);
        vector<int>right (nums.size(),1);

        int leftproduct = 1;
        for (int i = 0; i < nums.size(); ++i){
            left[i] = leftproduct;
            leftproduct *= nums[i];
        }

        int rightproduct = 1;
        for (int i = nums.size() -1; i >= 0; --i){
            right[i] = rightproduct;
            rightproduct *= nums[i];
        }

        vector<int> res (nums.size());

        for (int i = 0; i<nums.size(); i++){
            res[i] = right[i] * left[i];
        }
        return res;
    }
};