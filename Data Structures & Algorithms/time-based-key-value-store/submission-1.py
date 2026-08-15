class TimeMap:
    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashmap:
            value = self.hashmap[key]
            n = len(value)
            l = 0
            r = n-1
            res = -1
            while l <= r:
                mid = l + (r-l)//2
                if value[mid][0] <= timestamp:
                    l = mid + 1
                    res = mid
                else:
                    r = mid - 1
            if res == -1:
                return ""
            return value[res][1]
        else:
            return ""

