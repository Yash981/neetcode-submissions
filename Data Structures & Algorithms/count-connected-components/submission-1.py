class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u,v in edges:
            dsu.union(u,v)
            dsu.union(v,u)
        for i in range(n):
            dsu.find(i)
        return len(set(dsu.parent))        