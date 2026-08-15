from functools import lru_cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        @lru_cache(None)
        def dp(i,j):
            if j < 0:
                return False
            if i >= n:
                if j == 0:
                    return True
                return False
            ans = False
            if s[i] == "(":
                ans |= dp(i+1,j+1)
            elif s[i] == ")":
                ans |= dp(i+1,j-1)
            else:
                ans |= dp(i+1,j)
                ans |= dp(i+1,j-1)
                ans |= dp(i+1,j+1)
            return ans
        return dp(0,0)