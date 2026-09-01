class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # arr=[1,2,3,2,1,2,3,2,1]
        n = len(arr)
        def f(fla):
            ans = 0
            count = 0
            flag = 0
            for i in range(n-1):
                if arr[i] > arr[i+1]:
                    if flag == 0:
                        count = 1
                    else:
                        count += 1
                    flag = 0
                elif arr[i] < arr[i+1]:
                    if flag == 1:
                        count = 1
                    else:
                        count += 1
                    flag = 1
                else:
                    flag = -1
                    count = 0
                ans = max(ans,count)
            ans = max(ans,count)
            return ans + 1
        return max(f(True),f(False))