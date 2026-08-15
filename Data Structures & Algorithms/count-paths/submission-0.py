class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[-1] * (n+1) for _ in range(m+1)]
        def dp(i,j):
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            if cache[i][j] != -1:
                return cache[i][j]
            down = dp(i+1,j)
            right = dp(i,j+1)
            cache[i][j] = down + right
            return down +right
        return dp(0,0)