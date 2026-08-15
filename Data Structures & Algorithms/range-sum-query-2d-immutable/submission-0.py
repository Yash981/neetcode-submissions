class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.prefix_sum_matrix = [[0] * m for _ in range(n)]
        for x in range(n):
            for y in range(m):
                self.prefix_sum_matrix[x][y] = matrix[x][y]
                if x > 0:
                    self.prefix_sum_matrix[x][y] += self.prefix_sum_matrix[x-1][y]
                if y > 0:
                    self.prefix_sum_matrix[x][y] += self.prefix_sum_matrix[x][y-1]
                if x > 0 and y > 0:
                    self.prefix_sum_matrix[x][y] -= self.prefix_sum_matrix[x-1][y-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.querySum(row1,col1,row2,col2)

    def querySum(self,r1,c1,r2,c2):
        res = self.prefix_sum_matrix[r2][c2]
        if r1 > 0:
            res -= self.prefix_sum_matrix[r1-1][c2]
        if c1 > 0:
            res -= self.prefix_sum_matrix[r2][c1-1]
        if r1 > 0 and c1 > 0:
            res += self.prefix_sum_matrix[r1-1][c1-1]
        return res
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)