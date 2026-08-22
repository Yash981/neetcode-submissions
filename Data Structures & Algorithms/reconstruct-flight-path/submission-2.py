from sortedcontainers import SortedList
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        graph = defaultdict(SortedList)
        indegree = Counter()
        for u,v in tickets:
            graph[u].add(v)
        ans = []
        def dfs(node):
            while graph[node]:
                neighbour = graph[node].pop(0)
                dfs(neighbour)
            ans.append(node)
        dfs("JFK")
        # print(indegree)
        return ans[::-1]