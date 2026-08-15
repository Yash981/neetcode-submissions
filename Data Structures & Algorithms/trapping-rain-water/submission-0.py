class Solution:
    def trap(self, height: List[int]) -> int:
        def prefixFn(arr):
            m = len(arr)
            prefix = [arr[0]]
            for i in range(1,m):
                prefix.append(max(prefix[-1],arr[i]))
            return prefix
        pref = prefixFn(height)
        suff = prefixFn(height[::-1])[::-1]
        ans = 0
        for i in range(1,len(height)-1):
            left = pref[i]
            right = suff[i]
            ans += min(left,right) - height[i]
        return ans
            
