// Last updated: 10/21/2026, 9:38:07 PM
1class Solution {
2public:
3    bool isAnagram(string s, string t) {
4        unordered_map <char,int> S;
5        unordered_map  <char,int> T;
6
7        for (char& c: s){
8            if (S.count(c) == 0){
9                S[c] = 0;
10            }
11            S[c]+=1;
12        }
13
14        for (char& c: t){
15            if (T.count(c) == 0){
16                T[c] = 0;
17            }
18            T[c]+=1;
19        }
20
21        return S==T;
22
23
24    }
25};