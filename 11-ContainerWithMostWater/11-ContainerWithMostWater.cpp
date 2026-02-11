// Last updated: 2/11/2026, 11:08:47 AM
class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxarea = 0;
        int left = 0;
        int right = height.size()-1;

        while (left <right){
            if (height[left] > height[right]){
                int area = height[right] * (right-left);
                right--;
                if (area > maxarea) maxarea = area;
            }
            else{
                int area = height[left] * (right-left);
                left++;
                if (area > maxarea) maxarea = area;
            }
        }

        return maxarea;
    }
};