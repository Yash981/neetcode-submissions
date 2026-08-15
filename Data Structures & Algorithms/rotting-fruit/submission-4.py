class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def bfs(queue):
            steps = 0
            while queue:
                r,c,score = queue.popleft()
                steps = max(steps,score)
                for d in directions:
                    nr = d[0] + r
                    nc = d[1] + c
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        queue.append((nr,nc,score+1))
            return steps
        ans = 0
        currQueue = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    currQueue.append((i,j,0))
        ans = max(ans,bfs(currQueue))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return ans