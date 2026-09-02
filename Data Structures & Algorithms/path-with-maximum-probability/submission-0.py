import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i,(u,v) in enumerate(edges):
            graph[u].append([v,succProb[i]])
            graph[v].append([u,succProb[i]])
        hp = []
        heapq.heapify(hp)
        heapq.heappush(hp,(-1,start_node))
        dist = [-1e9] * n
        dist[start_node] = 1
        while hp:
            succ, currnode = heapq.heappop(hp)
            succ = -succ
            if currnode == end_node:
                return succ
            for neighbour,wgt in graph[currnode]:
                currweight = succ * wgt
                if dist[neighbour] < currweight:
                    dist[neighbour] = currweight
                    heapq.heappush(hp,(-currweight,neighbour))
        if dist[end_node] == -1e9:
            return 0
        return dist[end_node]