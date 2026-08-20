class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = 1e9

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val,val])
            self.mini = val
        else:
            self.mini = min(self.stack[-1][0],val)
            self.stack.append([self.mini,val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][1]

    def getMin(self) -> int:
        return self.stack[-1][0]
