// Last updated: 5/24/2026, 4:40:00 PM
1#include <climits>
2
3class Solution {
4public:
5    int removeDuplicates(vector<int>& nums) {
6        vector<int> temp = nums;
7        int curr = INT_MIN;
8        int index = 0;
9
10
11        for (int i = 0; i < temp.size();i ++){
12            if (temp[i] > curr){
13                nums[index] = temp[i];
14                curr = temp[i];
15                index++; 
16            }
17        }
18
19        return index;
20    }
21};