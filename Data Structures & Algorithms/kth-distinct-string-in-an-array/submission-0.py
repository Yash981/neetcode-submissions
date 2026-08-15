class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        ans = []
        for i in arr:
            if freq[i] == 1:
                ans.append(i)
        if len(ans) < k:
            return ""
        return ans[k-1]
