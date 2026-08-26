class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        parenstack = []
        remove = set()
        for i in range(n):
            if s[i] == "(":
                parenstack.append(i)
            elif s[i] == ")":
                if parenstack:
                    parenstack.pop()
                else:
                    remove.add(i)
        
        for i in parenstack:
            remove.add(i)
        return "".join([s[x] for x in range(n) if x not in remove])        
                
