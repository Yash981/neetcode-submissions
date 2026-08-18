from sortedcontainers import SortedList
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[1,0],[0,1],[-1,0],[0,-1],[-1,1],[-1,-1],[1,-1],[1,1]]
        queue = deque([])
        queue.append((1,0,0))
        visited = set()
        visited.add((0,0))
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        while queue:
            length,r,c = queue.popleft()
            if r == n-1 and c == n-1:
                return length
            for x,y in directions:
                nr = x + r
                nc = y + c
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((length+1,nr,nc))
        return -1