import bisect
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        x = float("-inf")
        y = float("-inf")
        z = float("-inf")
        for a,b,c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                x,y,z = max(x,a),max(y,b),max(z,c)
        return [x,y,z] == target
