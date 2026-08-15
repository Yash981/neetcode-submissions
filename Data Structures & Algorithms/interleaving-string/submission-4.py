class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        o = len(s3)
        if n+m != o:
            return False
        def dp(i,j,k):
            if k == o:
                return True
            res = False
            if i < n and s1[i] == s3[k]:
                res |= dp(i+1,j,k+1)
            if j < m and s2[j] == s3[k]:
                res |= dp(i,j+1,k+1)
            return res
        return dp(0,0,0)
