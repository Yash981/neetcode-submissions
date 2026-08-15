class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [1,1]
        if numRows == 1:
            return [[1]]
        ans = [[1],[1,1]]
        numRows -= 2
        while numRows:
            newarr = []
            for x in range(len(arr)-1):
                newarr.append(arr[x]+arr[x+1])
            arr = [1] + newarr + [1]
            ans.append(arr)
            numRows -= 1
        return ans