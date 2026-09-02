class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        arr = []
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                arr.append(1)
            else:
                arr.append(0)
        prefix = [0] + list(accumulate(arr))
        ans = []
        for l,r in queries:
            ans.append(prefix[r+1] - prefix[l])
        return ans