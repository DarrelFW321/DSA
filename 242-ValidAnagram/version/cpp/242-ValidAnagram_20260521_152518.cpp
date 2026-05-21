// Last updated: 5/21/2026, 3:25:18 PM
1class Solution {
2public:
3    bool isAnagram(string s, string t) {
4        unordered_map<char,int> s_map;
5        unordered_map<char,int> t_map;
6
7        for (char ch:s){
8            s_map[ch]++;
9        }
10
11        for (char ch : t){
12            t_map[ch]++;
13        }
14
15        if (s_map == t_map){
16            return true;
17        }
18
19        return false;
20    }
21};