from sortedcontainers import SortedList
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((v,t))
        hp = SortedList([(0,k)])
        distance = [1e9] * (n+1)
        distance[k] = 0
        while hp:
            time,node = hp.pop(0)
            if time != 0 and time > distance[node]:
                continue
            for neighbour, nghTime in graph[node]:
                if distance[neighbour] > time + nghTime:
                    distance[neighbour] = time + nghTime
                    hp.add((time+nghTime,neighbour))
        if any(i==1e9 for i in distance[1:]):
            return -1
        return max(distance[1:])

