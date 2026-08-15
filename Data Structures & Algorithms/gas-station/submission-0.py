class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas)-sum(cost) < 0:
            return -1
        i = 0
        currentCost = gas[i]
        target = n
        while i < target:
            if currentCost - cost[i%n] >= 0:
                currentCost = currentCost-cost[i%n] + gas[(i+1)%n]
                i += 1
            else:
                i = i+1
                target = i+n
                currentCost = gas[i]
        return i % n