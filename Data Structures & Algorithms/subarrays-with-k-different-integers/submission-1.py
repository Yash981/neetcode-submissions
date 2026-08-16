class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def f(target):
            i = 0
            j = 0
            hashmap = Counter()
            uniq = 0
            ans = 0

            while j < n:
                hashmap[nums[j]] += 1

                if hashmap[nums[j]] == 1:
                    uniq += 1

                # Keep removing while we still have >= target distinct
                while uniq >= target:
                    hashmap[nums[i]] -= 1

                    if hashmap[nums[i]] == 0:
                        uniq -= 1

                    i += 1

                # Now [i ... j] is the first window with < target distinct.
                # Therefore every starting point before i is valid.
                ans += i

                j += 1

            return ans

        return f(k) - f(k + 1)

