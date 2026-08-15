class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for x in range(m):
                        if matrix[i][x] != 0 and matrix[i][x] != '0':
                            matrix[i][x] = "0"
                    for y in range(n):
                        if matrix[y][j] != 0 and matrix[y][j] != "0":
                            matrix[y][j] = "0"
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0
        