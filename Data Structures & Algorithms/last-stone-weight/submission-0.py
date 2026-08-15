from sortedcontainers import SortedList
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = SortedList(stones)
        while len(hp) > 1:
            first_heavy = hp.pop()
            second_heavy = hp.pop()

            if first_heavy < second_heavy:
                hp.add(second_heavy-first_heavy)
            elif first_heavy > second_heavy:
                hp.add(-second_heavy+first_heavy)
        if not hp:
            return 0
        return hp[-1]

