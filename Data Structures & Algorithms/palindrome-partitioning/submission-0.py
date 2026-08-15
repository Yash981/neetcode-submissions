class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        def backtrack(i,stack):
            if i >= n:
                ans.append(stack[:])
                return
            for x in range(i,n):
                if s[i:x+1] == s[i:x+1][::-1]:
                    stack.append(s[i:x+1])
                    backtrack(x+1,stack)
                    stack.pop()
        backtrack(0,[])
        return ans
            
            