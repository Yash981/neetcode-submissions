class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # cardPoints=[96,90,41,82,39,74,64,50,30]
        # k=8
        # Expected output:
        # 536
        n = len(cardPoints)
        total = sum(cardPoints)
        if n == k:
            return total
        length = n-k
        ans = 0
        i = 0
        j = 0
        curr = 0
        while j < n:
            curr += cardPoints[j]
            if j - i + 1 < length:
                j += 1
            else:
                ans = max(ans,total-curr)
                curr -= cardPoints[i]
                i += 1
                j += 1
        return ans