class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroids += ["#"]
        n = len(asteroids)
        stack = []
        for x in range(n):
            while len(stack) > 1 and asteroids[stack[-2]] > 0  and asteroids[stack[-1]] < 0:
                poplast = stack.pop()
                poplastSecond = stack.pop()
                if abs(asteroids[poplast]) < abs(asteroids[poplastSecond]):
                    stack.append(poplastSecond)
                elif abs(asteroids[poplast]) > abs(asteroids[poplastSecond]):
                    stack.append(poplast)
            stack.append(x)
        stack.pop()
        ans = []
        for i in stack:
            ans.append(asteroids[i])
        return ans