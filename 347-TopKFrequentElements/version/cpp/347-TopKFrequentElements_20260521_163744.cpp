// Last updated: 5/21/2026, 4:37:44 PM
1class Solution {
2public:
3    vector<int> topKFrequent(vector<int>& nums, int k) {
4        vector<vector<int>> buckets(nums.size()+1);
5
6        unordered_map<int,int> mp; //num -> count 
7
8        for (int num: nums){
9            mp[num]++;
10        }
11
12        for (auto pair : mp){
13            buckets[pair.second].push_back(pair.first);
14        }
15        vector<int> res;
16        int count =0;
17        for (int i = nums.size(); i> 0; i--){
18            for (int num: buckets[i]){
19                res.push_back(num);
20                count++;
21            }
22            if (count == k ) break;
23        }
24
25        return res;
26    }
27};