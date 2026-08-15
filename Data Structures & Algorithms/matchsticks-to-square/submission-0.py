class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total//4
        matchsticks.sort(reverse=True)
        # print(matchsticks,target)
        used = [False] * n
        def backtrack(i,score,count):
            if i == n:
                if count == 3:
                    return True
                return False
            if score == target:
                return backtrack(0,0,count+1)
            for x in range(i,n):
                if not used[x]:
                    used[x] = True
                    if backtrack(x+1,score+matchsticks[x],count):
                        return True
                    used[x] = False
            return False
        return backtrack(0,0,0)