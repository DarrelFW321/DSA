// Last updated: 10/21/2026, 9:39:47 PM
1class Solution {
2public:
3    bool isAnagram(string s, string t) {
4        if (s.size() != t.size())return false;
5        
6        unordered_map <char,int> S;
7        unordered_map  <char,int> T;
8
9
10        for (char& c: s){
11            S[c]+=1;
12        }
13
14        for (char& c: t){
15            T[c]+=1;
16        }
17
18        return S==T;
19
20
21    }
22};