from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        @lru_cache(None)
        def dp(i):
            if i >= n:
                return True
            for x in range(i,n):
                curr = s[i:x+1]
                if curr in words:
                    if dp(x+1):
                        return True
            return False
        return dp(0)