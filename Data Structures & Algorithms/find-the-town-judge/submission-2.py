class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = [0] * n
        nobody = set()
        for i,j in trust:
            i -= 1
            j -= 1
            people[j] += 1
            nobody.add(i)
        print(people)
        for x in range(n):
            if people[x] != 0 and people[x] == n-1 and x not in nobody:
                return x+1
        return -1
        