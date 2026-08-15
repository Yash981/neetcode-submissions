from sortedcontainers import SortedList
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        def build_edges(points):
            edges = []
            for i in range(n):
                for j in range(i + 1, n): 
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    edges.append((dist, i, j))
                    edges.append((dist, j, i))
            
            return edges
        edges = build_edges(points)
        graph = defaultdict(list)
        for w,u,v in edges:
            graph[u].append((v,w))
        hp = SortedList([(0,0)])
        visited = set()
        ans = 0
        while hp:
            wgt,node = hp.pop(0)
            if node in visited:
                continue
            ans += wgt
            visited.add(node)
            for neighbour,weight in graph[node]:
                if neighbour not in visited:
                    hp.add((weight,neighbour))
        return ans
