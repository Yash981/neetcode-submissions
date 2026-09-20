class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        if n == 1:
            return 1

        ans = 1
        up = 0
        down = 0
        peak = 0

        for i in range(1, n):

            if ratings[i] > ratings[i - 1]:
                up += 1
                peak = up
                down = 0

                ans += up + 1

            elif ratings[i] < ratings[i - 1]:
                down += 1
                up = 0

                ans += down

                # Peak needs one extra candy if
                # decreasing slope becomes longer
                if down > peak:
                    ans += 1

            else:
                up = 0
                down = 0
                peak = 0
                ans += 1

        return ans