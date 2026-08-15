class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        i = 0
        j = 0
        hashtableS1 = Counter(s1)
        hashtableS2 = Counter()
        while j < m:
            hashtableS2[s2[j]] += 1
            if j-i+1 < n:
                j += 1
            else:
                if hashtableS2 == hashtableS1:
                    return True
                hashtableS2[s2[i]] -= 1
                if hashtableS2[s2[i]] == 0:
                    del hashtableS2[s2[i]]
                i += 1
                j += 1
        return False
            
