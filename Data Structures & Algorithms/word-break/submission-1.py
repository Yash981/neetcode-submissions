class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        cache = [-1] * n
        def dp(i):
            if i >= n:
                return True
            if cache[i] != -1:
                return cache[i]
            for x in range(i,n):
                if s[i:x+1] in wordDict:
                    if dp(x+1):
                        cache[i] = True
                        return True
            cache[i] = False
            return False
        return dp(0)