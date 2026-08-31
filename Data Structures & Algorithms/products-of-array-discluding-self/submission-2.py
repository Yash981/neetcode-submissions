class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]
        for i in range(n):
            prefix.append(prefix[-1] * nums[i])
        prefix = prefix[1:]
        suffix = [1]
        for i in range(n-1,-1,-1):
            suffix.append(suffix[-1] * nums[i])
        suffix = suffix[1:]
        suffix = suffix[::-1]

        # print(prefix)
        # print(suffix)
        ans = []
        for i in range(n):
            if i == 0:
                ans.append(suffix[i+1])
            elif i == n-1:
                ans.append(prefix[i-1])
            else:
                left = prefix[i-1]
                right = suffix[i+1]
                ans.append(left * right)
        return ans
