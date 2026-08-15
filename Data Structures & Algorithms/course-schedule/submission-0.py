class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        # print(indegree)
        queue = deque([])
        visited = set()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                visited.add(i)
        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    indegree[neighbour] -= 1
                    if indegree[neighbour] == 0:
                        queue.append(neighbour)
        return len(visited) == numCourses
        

