// Last updated: 5/24/2026, 4:40:36 PM
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
12            int val = temp[i];
13            if (temp[i] > curr){
14                nums[index] = val;
15                curr = val;
16                index++; 
17            }
18        }
19
20        return index;
21    }
22};