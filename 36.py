''' 
Question:

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set = {}
        for i in range(9):
            for j in range(9):
                target = board[i][j]
                if target != '.':
                    target_i, target_j = i, j
                else:
                    continue
                
                for k in range(9):
                    if target_j == k:
                        continue
                    else:
                        if target == board[i][k]:
                            return False
                
                for l in range(9):
                    if target_i == l:
                        continue
                    else:
                        if target == board[l][j]:
                            return False
                
                for n in range(9):
                    for m in range(9):
                        if n == target_i and m == target_j:
                            continue

                        if n//3 == target_i//3 and m//3 == target_j//3:
                            if target == board[n][m]:
                                return False
                    
        return True
            
