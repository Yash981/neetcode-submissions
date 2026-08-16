class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def f(target):
            i = 0
            j = 0
            hashmap = Counter()
            uniq = 0
            ans = 0

            while i < n:
                while j < n and uniq < target:
                    hashmap[nums[j]] += 1

                    if hashmap[nums[j]] == 1:
                        uniq += 1

                    j += 1

                # If we have target distinct values,
                # every extension to the right is valid.
                if uniq >= target:
                    ans += n - j + 1

                hashmap[nums[i]] -= 1

                if hashmap[nums[i]] == 0:
                    uniq -= 1

                i += 1

            return ans

        return f(k) - f(k + 1)

