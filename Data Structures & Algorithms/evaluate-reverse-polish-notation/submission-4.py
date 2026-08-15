class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        for i in range(n):
            if tokens[i] in "+*/-":
                if tokens[i] == "+":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val1+val2)
                if tokens[i] == "-":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2-val1)
                if tokens[i] == "*":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val1*val2)
                if tokens[i] == "/":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(int(val2/val1))
            else:
                stack.append(int(tokens[i]))
        return stack.pop()