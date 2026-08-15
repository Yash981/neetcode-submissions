class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        timeTakenByPosy = sorted([(pos, spd, (target - pos) / spd) for pos, spd in zip(position, speed)],key=lambda x: x[0],reverse=True)
        # print(timeTakenByPosy)
        stack = []
        for i,x in enumerate(timeTakenByPosy):
            if not stack:
                stack.append(x[2])
            else:
                if stack[-1] < x[2]:
                    stack.append(x[2])

        # print(stack)

        return len(set(stack))