// Last updated: 2/11/2026, 11:08:36 AM
#include <algorithm>
#include <vector>
using namespace std;



class Solution {
public:
    int trap(vector<int>& height) {
        int res = 0;

        vector<int>left(height.size(),0);
        vector<int>right(height.size(),0);

        int max = 0;

        for (int i = 0; i< height.size(); ++i){
            if (height[i] > max){
                max = height[i];
            }
            left[i]=max;
        }

        max = 0;

        for (int i = height.size()-1; i>=0; --i){
            if (height[i] > max){
                max = height[i];
            }
            right[i] = max;
        }

        for (int i = 0; i < height.size(); ++i){
            res+= min((left[i]-height[i]),(right[i]-height[i]));
        }

        return res;

    }
};