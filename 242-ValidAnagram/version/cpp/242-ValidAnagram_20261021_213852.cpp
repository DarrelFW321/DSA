// Last updated: 10/21/2026, 9:38:52 PM
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
11            if (S.count(c) == 0){
12                S[c] = 0;
13            }
14            S[c]+=1;
15        }
16
17        for (char& c: t){
18            if (T.count(c) == 0){
19                T[c] = 0;
20            }
21            T[c]+=1;
22        }
23
24        return S==T;
25
26
27    }
28};