class Solution:
    def isValid(self, s: str) -> bool:
        s += "#"
        stack = []
        for i in range(len(s)):
            while len(stack) > 1 and stack[-2] == "(" and stack[-1] == ")":
                stack.pop() 
                stack.pop() 
            while len(stack) > 1 and stack[-2] == "[" and stack[-1] == "]":
                stack.pop() 
                stack.pop() 
            while len(stack) > 1 and stack[-2] == "{" and stack[-1] == "}":
                stack.pop() 
                stack.pop() 
            stack.append(s[i])
        # print(stack)
        return len(stack[:-1]) == 0