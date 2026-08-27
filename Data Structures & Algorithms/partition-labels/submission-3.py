class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        h = defaultdict(list)
        for i,v in enumerate(s):
            if len(h[v]) > 1:
                h[v][-1] = i
            else:
                h[v].append(i)
                h[v].append(i)
        arr = [v for v in h.values()]
        # print(arr)
        m = len(arr)
        arr.sort()
        ans = []
        prevStart = arr[0][0]
        prevEnd = arr[0][1]
        for i in range(1,m):
            if prevEnd > arr[i][0]:
                prevStart = min(prevStart,arr[i][0])
                prevEnd = max(prevEnd,arr[i][1])
            else:
                ans.append(prevEnd - prevStart+1)
                prevStart = arr[i][0]
                prevEnd = arr[i][1]
        ans.append(prevEnd - prevStart+1)
        return ans