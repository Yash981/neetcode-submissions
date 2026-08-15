class Solution:
    def trap(self, height: List[int]) -> int:
        def prefixFn(arr):
            prefix = [arr[0]]
            for i in range(1,len(arr)):
                prefix.append(max(prefix[-1],arr[i]))
            return prefix
        pref = prefixFn(height)
        suff = prefixFn(height[::-1])[::-1]
        # print(pref)
        # print(suff)
        ans = 0
        for x in range(len(height)):
            ans += min(pref[x],suff[x]) - height[x]
        return ans
        