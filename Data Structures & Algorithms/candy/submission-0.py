class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        leftRating = [1] * n
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                leftRating[i] = max(leftRating[i],leftRating[i-1]+1)
        rightRating = [1] * n
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                rightRating[i] = max(rightRating[i],rightRating[i+1]+1)
        ans = 0
        for i in range(n):
            ans += max(leftRating[i],rightRating[i])
        return ans