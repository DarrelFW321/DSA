// Last updated: 11/10/2026, 10:30:27 PM
1#include <string>
2#include <vector>
3#include <unordered_map>
4using namespace std;
5
6class Solution {
7public:
8    vector<vector<string>> groupAnagrams(vector<string>& strs) {
9
10        unordered_map<string,vector<string>> dict;
11        
12        for (const string& str:strs){
13            vector<int> key(26,0);
14            for (char ch : str){
15                int index = ch - 'a';
16                key[index]++;
17            }
18            string hashkey = array_to_string(key);
19            dict[hashkey].push_back(str);
20        }
21
22        vector<vector<string>> res;
23
24        for (auto &[key,val]:dict){
25            res.push_back(val);
26        }
27
28        return res;
29
30
31
32
33
34    }
35
36    string array_to_string(vector<int>& arr){
37        string res;
38        for (int count : arr){
39            res += "#" + to_string(count);
40        }
41        return res;
42    }
43};