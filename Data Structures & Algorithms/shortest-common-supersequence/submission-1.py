class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if str1[i] == str2[j]:
                    if i > 0 and j > 0:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = 1
                else:
                    if i > 0:
                        dp[i][j] = max(dp[i-1][j],dp[i][j])
                    if j > 0:
                        dp[i][j] = max(dp[i][j],dp[i][j-1])
        i = n-1
        j = m-1
        ans = []
        while i >= 0 and j >= 0:

            # Same character -> take it once
            if str1[i] == str2[j]:
                ans.append(str1[i])
                i -= 1
                j -= 1

            # Move toward the larger LCS value
            elif i > 0 and j > 0:
                if dp[i - 1][j] >= dp[i][j - 1]:
                    ans.append(str1[i])
                    i -= 1
                else:
                    ans.append(str2[j])
                    j -= 1

            elif i > 0:
                ans.append(str1[i])
                i -= 1

            else:
                ans.append(str2[j])
                j -= 1

        # Remaining characters
        while i >= 0:
            ans.append(str1[i])
            i -= 1

        while j >= 0:
            ans.append(str2[j])
            j -= 1

        return ''.join(reversed(ans))