from sortedcontainers import SortedList
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        hp = SortedList([])
        hp.add((grid[0][0],0,0))
        visited = set()
        visited.add((0,0))
        while hp:
            time,r,c = hp.pop(0)
            if r == n-1 and c == n-1:
                return time
            for d in directions:
                nr = r + d[0]
                nc = c + d[1]
                if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    if time > grid[nr][nc]:
                        hp.add((time,nr,nc))
                    elif time < grid[nr][nc]:
                        hp.add((grid[nr][nc],nr,nc))
        return -1