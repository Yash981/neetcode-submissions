from sortedcontainers import SortedList
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def EuclideanDist(x1,y1,x2,y2):
            return math.sqrt((x1-x2)**2 + (y1-y2)**2)
        hp = SortedList([])
        for x,y in points:
            dist = EuclideanDist(0,0,x,y)
            hp.add([dist,[x,y]])
            if len(hp) > k:
                hp.pop()
        return [i[1] for i in hp]