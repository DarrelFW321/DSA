// Last updated: 11/3/2026, 9:20:37 PM
1#include <algorithm>
2#include <string>
3
4class Solution {
5public:
6    vector<vector<string>> groupAnagrams(vector<string>& strs) {
7        std::unordered_map<std::string,std::vector<std::string>> dict;
8
9        for (std::string & str :strs){
10            std::string key = str;
11            std::sort(key.begin(),key.end());
12            dict[key].push_back(str);
13        }
14
15        std::vector<std::vector<string>> res;
16
17        for (auto &[key,val] : dict){
18            res.push_back(val);
19        }
20
21        return res;
22    }
23};