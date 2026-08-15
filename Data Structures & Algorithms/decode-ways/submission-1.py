class Solution:
    def numDecodings(self, s: str) -> int:
        hashtable = Counter()
        for i in range(1,27):
            hashtable[str(i)] = chr(i-1+65)
        n = len(s)
        memo = [-1] * n
        def dp(i):
            if i >= n:
                return 1
            if memo[i] != -1:
                return memo[i]
            ans = 0
            for x in range(i,n):
                dec = s[i:x+1]
                m = len(dec)
                if m <= 2 and dec in hashtable:
                    ans += dp(x+1)
                else:
                    break
            memo[i] = ans
            return ans
        return dp(0)