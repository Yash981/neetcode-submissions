class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        start = 0
        end = 0
        def f(l,r):
            nonlocal ans
            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1            
        for i in range(n):
            f(i,i)
            f(i,i+1)
        return ans