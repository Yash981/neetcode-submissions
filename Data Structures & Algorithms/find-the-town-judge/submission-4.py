class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = [0] * (n+1)
        for i,j in trust:
            people[i] -= 1
            people[j] += 1
        for x in range(1,n+1):
            if people[x] != 0 and people[x] == n-1:
                return x 
        return -1
        