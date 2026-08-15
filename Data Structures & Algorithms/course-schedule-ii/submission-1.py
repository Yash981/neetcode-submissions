class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        print(indegree)
        print(graph)
        queue = deque([])
        visited = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            node = queue.popleft()
            visited.append(node)
            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        return visited if len(visited) == numCourses else []