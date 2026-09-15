import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # intervals=[[2,3],[2,5],[1,8],[20,25]]
        # queries=[2,19,5,22]
        # #curr: [2,8,2,6]
        # # exp:[2,-1,4,6]
        n = len(queries)
        hp = []
        for x,y in intervals:
            length = y-x+1
            heapq.heappush(hp,[x,y,length])
        # print(hp)
        ans = [-1] * n
        hmap = defaultdict(list)
        for i,q in enumerate(queries):
            hmap[q].append(i)
        # print(hmap)
        queries.sort()
        newHp = []
        for q in queries:
            while hp and hp[0][0] <= q:
                x,y,length = heapq.heappop(hp)
                heapq.heappush(newHp,[length,x,y])
            while newHp and newHp[0][2] < q:
                heapq.heappop(newHp)
            if newHp and newHp[0][1] <= q <= newHp[0][2]:
                index = 0
                arr = hmap[q]
                m = len(arr)
                while index < m:
                    ans[arr[index]] = newHp[0][0]
                    index += 1
        return ans