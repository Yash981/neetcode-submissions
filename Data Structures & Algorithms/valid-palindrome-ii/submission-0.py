class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(n):
            if s[:i] + s[i+1:] == (s[:i] + s[i+1:])[::-1]:
                return True
        return False