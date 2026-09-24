import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        hp = []
        for x,y in zip(profits,capital):
            heapq.heappush(hp,[y,x])
        current = w
        newHp = []
        ans = 0
        while k:
            while hp and hp[0][0] <= current:
                currCap, currPro = heapq.heappop(hp)
                heapq.heappush(newHp,-currPro)
            if newHp:
                currPro2 = heapq.heappop(newHp)
                currPro2 = -currPro2
                current += currPro2
            k -= 1
        return current
            
            
