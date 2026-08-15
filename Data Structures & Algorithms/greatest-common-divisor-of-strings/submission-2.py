class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        mn = min(n,m)
        ans = ""
        for x in range(mn):
            pref = str1[:x+1]
            length = len(pref)
            if n % length == 0 and pref * (n//length) == str1 and m % length == 0 and pref*(m//length) == str2:
                 ans = pref
        return ans