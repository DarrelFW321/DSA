// Last updated: 11/3/2026, 10:05:04 PM
1class Solution {
2public:
3    vector<int> topKFrequent(vector<int>& nums, int k) {
4        std::unordered_map<int,int> freq;
5
6        for (auto num:nums){
7            freq[num]++;
8        }
9
10        std::vector<std::vector<int>>buckets(nums.size()+1);
11
12        for (const auto& [num,count]:freq){
13            buckets[count].push_back(num);
14        }
15
16        std::vector<int>res;
17
18        for (int i = nums.size(); i >=0; --i){
19            for (int num: buckets[i]){
20                res.push_back(num);
21
22                if (res.size() == k) return res;
23            }
24        }
25
26        return {};
27    }
28};