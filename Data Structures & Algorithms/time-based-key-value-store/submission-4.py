from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.freq = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.freq[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.freq[key]
        # print(arr)
        n = len(arr)
        l = 0
        r = n-1
        ans = -1
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid][1] <= timestamp:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        if ans == -1:
            return ""
        return arr[ans][0]
