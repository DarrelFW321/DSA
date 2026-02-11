# Last updated: 2/11/2026, 11:08:41 AM
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)] 
        column = [set() for _ in range(9)] 
        block = [set() for _ in range(9)] 

        for row_index, row_arr in enumerate(board):
            for column_index, char in enumerate(row_arr):
                if char == ".":
                    continue
                if char in row[row_index]:
                    return False
                
                if char in column[column_index]:
                    return False

                curr_block = row_index//3 + (column_index//3)*3

                if char in block[curr_block]:
                    return False
                
                row[row_index].add(char)
                column[column_index].add(char)
                block[curr_block].add(char)

        return True
