class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
    def find(self,x):
        if x == self.parent[x]:
            return x
        return self.find(self.parent[x])
    def union(self,x,y):
        rootA = self.find(x)
        rootB = self.find(y)
        if rootA == rootB:
            return True
        self.parent[rootB] = rootA
        return False        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        def manhattanDist(x1,y1,x2,y2):
            return abs(x1-x2) + abs(y1-y2)
        weighted = []
        for i in range(n):
            for j in range(i+1,n):
                weighted.append([manhattanDist(points[i][0],points[i][1],points[j][0],points[j][1]),i,j])
        weighted.sort()
        # print(weighted)
        dsu = DSU(n)
        left = set()
        right = set()
        ans = 0
        for val,x,y in weighted:
            res = dsu.union(x,y)
            if not res:
                ans += val
        return ans