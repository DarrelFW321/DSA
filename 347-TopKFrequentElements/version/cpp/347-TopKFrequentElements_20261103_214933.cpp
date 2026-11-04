// Last updated: 11/3/2026, 9:49:33 PM
1class Solution {
2public:
3    vector<int> topKFrequent(vector<int>& nums, int k) {
4        std::unordered_map<int,int>dict;
5
6        for (const int  num:nums){
7            dict[num]++;
8        }
9
10        std::priority_queue<std::pair<int,int>> minheap;
11
12        for (const auto &[key,val] : dict){
13            std::pair<int,int> node = {-val,key};
14            minheap.push(node);
15            while (minheap.size()>k) minheap.pop();
16        }
17
18        std::vector<int> res;
19
20        while (minheap.size()>0){
21            res.push_back(minheap.top().second);
22            minheap.pop();
23        }
24
25        return res;
26    }
27};