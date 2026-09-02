class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        prev = prices[0]
        for i in range(1,n):
            if prev >= prices[i]:
                prev = prices[i]
            else:
                ans += prices[i] - prev
                prev = prices[i]
        return ans
        