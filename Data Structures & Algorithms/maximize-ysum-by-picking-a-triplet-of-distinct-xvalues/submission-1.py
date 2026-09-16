class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        n = len(x)
        arr = []
        for i,j in zip(x,y):
            arr.append([j,i])
        arr.sort(reverse=True)
        # print(arr)
        seen = set()
        ans = 0
        for pair in arr:
            if len(seen) == 3:
                break
            if pair[1] not in seen:
                ans += pair[0]
                seen.add(pair[1])
        # print(seen)
        if len(seen) != 3:
            return -1
        return ans