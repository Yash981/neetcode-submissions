class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        l = max(weights)
        r = sum(weights)
        def isPossible(mid):
            day = 1
            curr = 0
            for x in weights:
                if curr+x <= mid:
                    curr += x
                else:
                    day += 1
                    curr = x
            return day <= days
        ans = -1
        while l <= r:
            mid = l + (r-l)//2
            if isPossible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
