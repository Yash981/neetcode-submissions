from sortedcontainers import SortedList
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hp = SortedList(Counter(tasks).values())
        mnCycles = 0
        queue = deque()
        while hp or queue:
            mnCycles += 1
            if queue and queue[0][-1] == mnCycles:
                freq,_ = queue.popleft()
                hp.add(freq)
            if hp:
                freq = hp.pop()
                freq -= 1
                if freq:
                    queue.append((freq,mnCycles+n+1))
        return mnCycles