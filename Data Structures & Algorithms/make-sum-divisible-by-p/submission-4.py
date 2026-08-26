class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # nums=[45,262,270,364,232,59,206,139,266,84,309,114,309,163,379,302,93,198,345,278,317,59,289,84,265,158,376,57,289,369,243,286,380,3,44,65,152,180,91,377,366,14,199,266,133,286,192,163,84,232,7,180,107,178,30,291,221,167,153,204,189,328,134,368,287,238,383,378,84,230,303,228,279,213,308,190,353]
        # p=1376
        # nums=[26,19,11,14,18,4,7,1,30,23,19,8,10,6,26,3]
        # p=26
        n = len(nums)
        total = sum(nums)
        # print(total)
        rem = total % p
        # print(rem)
        if rem == 0:
            return 0
        prefix = 0
        hashmap = Counter()
        hashmap[0] = -1
        ans = n
        for i in range(n):
            prefix = (prefix + nums[i]) % p
            if (prefix - rem + p) % p in hashmap:
                ans = min(ans,i-hashmap[(prefix - rem + p) % p])
            hashmap[prefix] = i
        return ans if ans != n else -1
        
            