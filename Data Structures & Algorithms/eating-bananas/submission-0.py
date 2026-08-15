class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def Ispossible(k):
            res = 0
            for pile in piles:
                if pile <= k:
                    res += 1
                else:
                    res += math.ceil(pile/k)
            return res <= h
        l = 1
        r = max(piles)
        ans = 1e9
        while l <= r:
            mid = l + (r-l)//2
            if Ispossible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans