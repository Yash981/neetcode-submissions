class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        hashtable = Counter()
        hashtable[0] = 1
        n = len(nums)
        ans = 0
        for i in range(n):
            prefixSum += nums[i]
            if prefixSum - k in hashtable:
                ans += hashtable[prefixSum - k]
            hashtable[prefixSum] += 1
        return ans