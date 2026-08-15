class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pacificPoints = deque([])
        visited1 = set()
        visited2 = set()
        atlanticPoints = deque([])
        for i in range(m):
            pacificPoints.append([0,i])
            visited1.add((0,i))
            atlanticPoints.append([n-1,i])
            visited2.add((n-1,i))
        for i in range(n):
            pacificPoints.append([i,0])
            visited1.add((i,0))
            atlanticPoints.append([i,m-1])
            visited2.add((i,m-1))
        pacific2dGrid = [[-1] * m for _ in range(n)]
        atlantic2dGrid = [[-1] * m for _ in range(n)]
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def bfs(queue,visited,grid):
            while queue:
                r,c = queue.popleft()
                grid[r][c] = 1
                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]
                    if 0 <= nr < n and 0 <= nc < m and heights[nr][nc] >= heights[r][c] and (nr,nc) not in visited:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
            
            return grid
        grid1 = bfs(pacificPoints,visited1,pacific2dGrid)
        grid2 = bfs(atlanticPoints,visited2,atlantic2dGrid)
        ans = []
        for x in range(n):
            for y in range(m):
                if grid1[x][y] == grid2[x][y] == 1:
                    ans.append([x,y])
        return ans