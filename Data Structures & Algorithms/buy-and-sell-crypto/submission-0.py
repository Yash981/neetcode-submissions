class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        ans = 0
        for i in range(1,len(prices)):
            ans = max(ans,prices[i]-mini)
            mini = min(prices[i],mini)
        return ans