from math import ceil,floor
import bisect
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n2 = len(nums2)
        def isPossible(mid):
            count = 0
            for x in nums1:
                if x > 0:
                    threshold = floor(mid/x)
                    index = bisect.bisect_right(nums2,threshold)
                    count += index
                elif x < 0:
                    threshold = ceil(mid/x)
                    index = bisect.bisect_left(nums2,threshold)
                    count += n2 - index
                else:
                    if mid >= 0:
                        count += n2
            return count >= k

        l = -(10**10)
        r = 10**10
        ans = 10**10
        while l <= r:
            mid = l + (r-l)//2
            if isPossible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans