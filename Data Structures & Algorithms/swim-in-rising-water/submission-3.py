import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        hp = []
        heapq.heappush(hp,(grid[0][0],0,0))
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        visited.add((0,0))
        while hp:
            currTime,r,c = heapq.heappop(hp)
            if r == n-1 and c == m-1:
                return currTime
            for x,y in directions:
                nr = r + x
                nc = c + y
                if 0 <= nr < n and 0 <= nc < m and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    heapq.heappush(hp,(max(grid[nr][nc],currTime),nr,nc))
        return -1
        

            

