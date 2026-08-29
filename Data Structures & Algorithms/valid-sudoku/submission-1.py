class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSeen = set()
        colSeen = set()
        boxSeen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                val = int(board[i][j])
                if (val,i) in rowSeen:
                    return False
                if (val,j) in colSeen:
                    return False
                if (val,(i//3)*3+(j//3)) in boxSeen:
                    return False
                rowSeen.add((val,i))
                colSeen.add((val,j))
                boxSeen.add((val,(i//3)*3+(j//3)))
        return True