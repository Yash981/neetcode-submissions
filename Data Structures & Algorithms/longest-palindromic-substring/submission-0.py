class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = 1
        start = 0
        end = 0
        def f(l,r):
            nonlocal ans,start,end
            while l >= 0 and r < n and s[l] == s[r]:
                if ans < r-l+1:
                    ans = r-l+1
                    start = l
                    end = r
                l -= 1
                r += 1            
        for i in range(n):
            f(i,i)
            f(i,i+1)
        return s[start:end+1]