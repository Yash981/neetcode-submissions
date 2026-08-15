class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(openN,closedN,s):
            if openN == closedN == n:
                res.append(s)
                return
            if openN < n:
                backtrack(openN+1,closedN,s+"(")
            if closedN < openN:
                backtrack(openN,closedN+1,s+")")
        backtrack(0,0,"")
        return res