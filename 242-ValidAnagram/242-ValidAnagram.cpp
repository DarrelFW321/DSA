// Last updated: 2/11/2026, 11:08:23 AM
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> map_s;
        unordered_map<char,int> mapt;

        if (size(t)!= size(s)){
            return false;
        }
        for(int i = 0; i < size(s); ++i){
            auto it = map_s.find(s[i]);
            if (it != map_s.end()){
                map_s[s[i]] +=1;
            }else{
                map_s[s[i]] = 1;
            }
        }

        for(int i = 0; i < size(t); ++i){
            auto it = mapt.find(t[i]);
            if (it != mapt.end()){
                mapt[t[i]] +=1;
            }else{
                mapt[t[i]] = 1;
            }
        }

        for (auto &[key,value] :map_s){
            if (mapt.find(key) == mapt.end()){
                return false;
            }
            if(value != mapt[key]){
                return false;
            }
        }

        return true;
    }
};