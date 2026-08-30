class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        # Instead of calculating the average directly, consider the total sum required for a sub-array of size `k` to meet the `threshold`. Average = Sum / k, so Sum must be >= `threshold * k`.
        i = 0
        j = 0
        target = threshold * k
        currsum = 0
        ans = 0
        while j < n:
            currsum += arr[j]
            if j >= k - 1:
                if currsum >= target:
                    ans += 1
                currsum -= arr[i]
                i += 1
            j += 1
        return ans
        

