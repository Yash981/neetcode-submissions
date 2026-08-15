class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        queue = deque([])
        for i in range(m):
            if board[0][i] == "O":
                queue.append((0,i))
                board[0][i] = "-1"
            if board[n-1][i] == "O":
                queue.append((n-1,i))
                board[n-1][i] = "-1"
        for i in range(1,n-1):
            if board[i][0] == "O":
                queue.append((i,0))
                board[i][0] = "-1"
            if board[i][m-1] == "O":
                queue.append((i,m-1))
                board[i][m-1] = "-1"
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while queue:
            r,c = queue.popleft()
            for d in directions:
                nr = d[0] + r
                nc = d[1] + c
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == "O":
                    board[nr][nc] = "-1"
                    queue.append((nr,nc))
        for i in range(n):
            for j in range(m):
                if board[i][j] == "-1":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

        
