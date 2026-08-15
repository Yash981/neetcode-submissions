class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)
        memo = Counter()
        def dp(i,currSum1,currSum2):
            if i >= n:
                return abs(currSum1 - currSum2)
            if (i,currSum1,currSum2) in memo:
                return memo[(i,currSum1,currSum2)]
            take = dp(i+1,currSum1+stones[i],currSum2-stones[i])
            notTake = dp(i+1,currSum1,currSum2)
            memo[(i,currSum1,currSum2)] = min(take,notTake)
            return min(take,notTake)
        return dp(0,0,total)