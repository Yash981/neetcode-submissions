class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        queue = deque([])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(i,j):
            for x,y in directions:
                ni = x + i
                nj = y + j
                if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and grid[ni][nj] == 1:
                    visited[ni][nj] = True
                    queue.append([ni,nj])
                    dfs(ni,nj)
        isLand1 = deque([])
        isLand2 = deque([])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    queue.append([i,j])
                    dfs(i,j)
                    if not isLand1:
                        isLand1 = queue
                    else:
                        isLand2 = queue
                    queue = deque([])
        print(isLand1)
        print(isLand2)
        ans = 1e9
        for x1,y1 in isLand1:
            for x2,y2 in isLand2:
                ans = min(ans,abs(x2-x1)+abs(y2-y1))
        return max(0,ans-1)
