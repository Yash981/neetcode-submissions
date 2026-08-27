class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        queue = deque([])
        visited = set()
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1) and board[i][j] == "O":
                    queue.append([i,j])
                    visited.add((i,j))
                if (j == 0 or j == m-1) and board[i][j] == "O":
                    queue.append([i,j])
                    visited.add((i,j))
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while queue:
            r,c = queue.popleft()
            for x,y in directions:
                nr = x + r
                nc = y + c
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == "O" and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr,nc))
        for x in range(n):
            for y in range(m):
                if board[x][y] == "O" and (x,y) not in visited:
                    board[x][y] = "X"
        
        
                