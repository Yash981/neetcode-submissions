from itertools import accumulate
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        arr = []
        for word in words:
            if word[0] in "aeiou" and word[-1] in "aeiou":
                arr.append(1)
            else:
                arr.append(0)
        prefix = [0] + list(accumulate(arr))
        ans = []
        for x,y in queries:
            ans.append(prefix[y+1]-prefix[x])
        return ans