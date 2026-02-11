// Last updated: 2/11/2026, 11:08:38 AM
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> row (9);
        vector<unordered_set<char>> column (9);
        vector<unordered_set<char>> block (9);

        for (int row_index = 0; row_index < 9; ++row_index){
            for (int column_index = 0; column_index <9; ++column_index){
                char ch = board[row_index][column_index];
                if (ch == '.'){
                    continue;
                }

                if (row[row_index].find(ch)!= row[row_index].end()){
                    return false;
                }
                if (column[column_index].find(ch)!= column[column_index].end()){
                    return false;
                }

                int curr_block = row_index/3 + (column_index/3) * 3;
                
                if (block[curr_block].find(ch)!= block[curr_block].end()){
                    return false;
                }
                
                row[row_index].insert(ch);
                column[column_index].insert(ch);
                block[curr_block].insert(ch);

            }
        }
        return true;
    }
};