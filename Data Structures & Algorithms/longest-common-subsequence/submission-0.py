class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        cache = [[-1] * (m+1) for _ in range(n+1)]
        def dp(i,j):
            if i >= n or j >= m:
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            ans = 0
            if text1[i] == text2[j]:
                ans = max(ans,1  + dp(i+1,j+1))
            else:
                ans = max(ans,dp(i+1,j),dp(i,j+1))
            cache[i][j] = ans
            return ans
        return dp(0,0)