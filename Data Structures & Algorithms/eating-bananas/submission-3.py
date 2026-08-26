class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        def isPossible(mid):
            hours = 0
            for x in piles:
                if x < mid:
                    hours += 1
                else:
                    quo = x//mid
                    rem = x % mid
                    if rem > 0:
                        quo += 1
                    hours += quo
            return hours <= h
        l = 1
        r = max(piles)
        ans = max(piles)
        while l <= r:
            mid = l+(r-l)//2
            if isPossible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
            
