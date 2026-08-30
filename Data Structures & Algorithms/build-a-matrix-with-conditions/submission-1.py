class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * k for _ in range(k)]
        graph = defaultdict(list)
        n = len(rowConditions)
        m = len(colConditions)
        rowIndegree = [0] * (k+1)
        for x,y in rowConditions:
            rowIndegree[y] += 1
            graph[x].append(y)
        # print(graph,rowIndegree)
        queue = deque([])
        for i in range(1,k+1):
            if rowIndegree[i] == 0:
                queue.append(i)
        rowOrder = []
        while queue:
            node = queue.popleft()
            rowOrder.append(node)
            for neighbour in graph[node]:
                rowIndegree[neighbour] -= 1
                if rowIndegree[neighbour] == 0:
                    queue.append(neighbour)
        if len(rowOrder) != k:
            return []
        # print(rowOrder)
        graph2 = defaultdict(list)
        colIndegree = [0] * (k+1)
        for x,y in colConditions:
            colIndegree[y] += 1
            graph2[x].append(y)
        # print(graph2,colIndegree)
        queue2 = deque([])
        for i in range(1,k+1):
            if colIndegree[i] == 0:
                queue2.append(i)
        colOrder = []
        while queue2:
            node = queue2.popleft()
            colOrder.append(node)
            for neighbour in graph2[node]:
                colIndegree[neighbour] -= 1
                if colIndegree[neighbour] == 0:
                    queue2.append(neighbour)
        if len(colOrder) != k:
            return []
        hmap1 = Counter()
        hmap2 = Counter()
        for i,x in enumerate(rowOrder):
            hmap1[x] = i
        for i,x in enumerate(colOrder):
            hmap2[x] = i
        # print(hmap1)
        # print(hmap2)
        for i in range(1,k+1):
            matrix[hmap1[i]][hmap2[i]] = i
        return matrix
        

            
