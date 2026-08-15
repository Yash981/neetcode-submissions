class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        queue = deque([(sr,sc)])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        while queue:
            r,c = queue.popleft()
            if (r,c) in visited:
                continue
            visited.add((r,c))
            prev = image[r][c]
            image[r][c] = color
            for x,y in directions:
                nr = x + r
                nc = y + c
                if 0 <= nr < n and 0 <= nc < m and image[nr][nc] == prev:
                    queue.append((nr,nc))
        
        return image
