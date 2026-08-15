from sortedcontainers import SortedList
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.hp = SortedList([])
        self.k = k
        x = self.k
        while x and nums:
            self.hp.add(nums.pop())
            x -= 1

    def add(self, val: int) -> int:
        self.hp.add(val)
        if len(self.hp) > self.k:
            self.hp.pop(0)
        return self.hp[-self.k]
