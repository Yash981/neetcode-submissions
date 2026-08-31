class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        queryMapping = defaultdict(list)
        for i,x in enumerate(queries):
            queryMapping[x].append(i)
        m = len(queries)
        queries = sorted(set(queries))
        length = len(queries)
        res = [-1] * m
        intervals.sort()
        i = 0
        j = 0
        hp = []
        while j < length:
            while i < n and intervals[i][0] <= queries[j]:
                heapq.heappush(hp,(intervals[i][1]-intervals[i][0]+1,intervals[i][0],intervals[i][1]))
                i += 1
            while hp and hp[0][2] < queries[j]:
                heapq.heappop(hp)
            if hp and hp[0][1] <= queries[j] <= hp[0][2]:
                for idx in  queryMapping[queries[j]]:
                    res[idx] = hp[0][0]
            j += 1
        return res

            
