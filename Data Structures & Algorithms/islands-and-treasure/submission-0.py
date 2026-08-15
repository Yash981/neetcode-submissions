class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        INF = 2147483647
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def bfs(i,j,used):
            queue = deque([(i,j,0)])
            while queue:
                r,c,steps = queue.popleft()
                if grid[r][c] == 0:
                    return steps
                for d in directions:
                    nr = d[0] + r
                    nc = d[1] + c
                    if 0 <= nr < n and 0 <= nc < m and (nr,nc) not in used and grid[nr][nc] != -1:
                        used.add((nr,nc))
                        queue.append((nr,nc,steps+1))
        for i in range(n):
            for j in range(m):
                used = set()
                if grid[i][j] == INF:
                    used.add((i,j))
                    steps = bfs(i,j,used)
                    grid[i][j] = steps
        
