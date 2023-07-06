class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checker = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue

                box = (i//3,j//3)
                if board[i][j] in checker[i] or board[i][j] in checker[j+9] or board[i][j] in checker[box]:
                    return False
                else:
                    checker[i].add(board[i][j])
                    checker[j+9].add(board[i][j])
                    checker[box].add(board[i][j])
        #print(checker)
        return True
