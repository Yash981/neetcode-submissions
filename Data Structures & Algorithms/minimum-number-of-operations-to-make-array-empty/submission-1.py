class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0
        for k,v in freq.items():
            if v == 1:
                return -1
            elif v % 3 == 0:
                print(v,"if")
                ans += v//3
            elif v % 3 == 1:
                ans += (v-4)//3 + 2
            else: # v % 3 == 2
                ans += (v-2)//3 + 1
        return ans