from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # (cost, stops, node)
        heap = [(0, 0, src)]
        
        # Best known (node, stops) pair
        visited = dict()

        while heap:
            cost, stops, node = heappop(heap)
            
            if node == dst:
                return cost
            
            if stops > k:
                continue
            
            # Only skip if we've seen better path with *same or fewer* stops
            if (node in visited and visited[node] <= stops):
                continue
            visited[node] = stops
            
            for nei, price in graph[node]:
                heappush(heap, (cost + price, stops + 1, nei))
        
        return -1

            