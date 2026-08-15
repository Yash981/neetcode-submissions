class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r,c,index,visited):
            if index == len(word):
                return True
            if r > n or c > m:
                return 0
            ans = False
            for d in directions:
                newRow = d[0] + r
                newCol = d[1] + c
                if 0 <= newRow < n and 0 <= newCol < m and (newRow,newCol) not in visited and board[newRow][newCol] == word[index]:
                    visited.add((newRow,newCol))
                    ans |= dfs(newRow,newCol,index+1,visited)
                    visited.remove((newRow,newCol))
            return ans
        ans = False
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i,j))
                    ans |= dfs(i,j,1,visited)
        return ans