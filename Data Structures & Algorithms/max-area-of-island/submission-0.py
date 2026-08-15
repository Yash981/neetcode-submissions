class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        def bfs(x,y):
            res = 1
            queue = deque([(x,y)])
            while queue:
                row,col = queue.popleft()
                for d in directions:
                    nr = d[0] + row
                    nc = d[1] + col
                    if 0 <= nr < n and 0 <= nc < m and (nr,nc) not in visited and grid[nr][nc] == 1:
                        res += 1
                        visited.add((nr,nc))
                        queue.append((nr,nc))
            return res
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i,j) not in visited:
                    visited.add((i,j))
                    ans = max(ans,bfs(i,j))
        return ans
