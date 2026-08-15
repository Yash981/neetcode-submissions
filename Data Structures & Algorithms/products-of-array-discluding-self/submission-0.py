class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        def prefixFn(arr):
            prefixProduct = [arr[0]]
            n = len(arr)
            for i in range(1,n):
                prefixProduct.append(prefixProduct[-1] * arr[i])
            return prefixProduct
        prefix = prefixFn(nums)
        suffix = prefixFn(nums[::-1])[::-1]
        ans = [suffix[1]]

        for i in range(1,length):
            left = prefix[i-1]
            right = 1
            if i+1 < length:
                right = suffix[i+1]
            ans.append(left * right)
        return ans

        
