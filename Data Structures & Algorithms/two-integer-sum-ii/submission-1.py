class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = Counter()
        for i,x in enumerate(numbers):
            diff = target - x
            if diff in hashmap:
                return [hashmap[diff]+1,i+1]
            hashmap[x] = i
        return [-1,-1]