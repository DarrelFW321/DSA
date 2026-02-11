// Last updated: 2/11/2026, 11:08:33 AM
#include <cctype>
#include <string>
using namespace std;


class Solution {
public:
    bool isPalindrome(string s) {
        string cleaned = "";
        for (auto ch: s){
            if (isalnum(ch)){
                cleaned += tolower(ch);
            }
        }

        for (int i = 0, j =cleaned.size()-1; i < cleaned.size()/2; ++i,--j){
            if (cleaned[i] != cleaned[j]){
                return false;
            }

        }

        return true;


        
    }
};