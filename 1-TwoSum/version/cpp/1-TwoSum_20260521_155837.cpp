// Last updated: 5/21/2026, 3:58:37 PM
1class Solution {
2public:
3    vector<vector<string>> groupAnagrams(vector<string>& strs) {
4        unordered_map<string,vector<string>> dicts;
5        
6        for (string str: strs){
7            string key = str;
8            sort(key.begin(),key.end());
9            dicts[key].push_back(str);
10        }
11
12        vector<vector<string>> res;
13        for (auto pair: dicts){
14            res.push_back(pair.second);
15        }
16
17        return res;
18
19    }
20};