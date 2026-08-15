from sortedcontainers import SortedList
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacencyList = defaultdict(list)
        for s,e,cost in flights:
            adjacencyList[s].append((e,cost))


        hp = SortedList([(0,0,src)])
        distance = [1e9] * n
        distance[src] =  0
        while hp:
            stops,cost,city = hp.pop(0)
            for neighbour,neighCost in adjacencyList[city]:
                if distance[neighbour] > cost+neighCost and stops <= k:
                    distance[neighbour] = cost+neighCost
                    hp.add((stops+1,cost+neighCost,neighbour))
        return -1 if distance[dst] == 1e9 else distance[dst]
            