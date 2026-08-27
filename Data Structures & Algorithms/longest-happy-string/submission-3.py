import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        hp = []
        if a > 0:
            heapq.heappush(hp,[-a,'a'])
        if b > 0:
            heapq.heappush(hp,[-b,'b'])
        if c > 0:
            heapq.heappush(hp,[-c,'c'])
        ans = []
        while hp:
            first,char1 = heapq.heappop(hp)
            first = -first
            if len(ans) > 1 and ans[-1] == ans[-2] == char1:
                if not hp:
                    break
                second,char2 = heapq.heappop(hp)
                second = -second
                ans.append(char2)
                second -= 1
                if second > 0:
                    heapq.heappush(hp,[-second,char2])
                heapq.heappush(hp,[-first,char1])
            else:
                ans.append(char1)
                first -= 1
                if first > 0:
                    heapq.heappush(hp,[-first,char1])
        return "".join(ans)
            