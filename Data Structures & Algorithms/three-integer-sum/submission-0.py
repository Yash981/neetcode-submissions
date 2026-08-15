class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        for i in range(n-2):
            currentNum = nums[i]
            new_arr = sorted(nums[i+1:])
            m = len(new_arr)
            j = 0
            k = m-1
            while j < k:
                if currentNum + new_arr[j] + new_arr[k] == 0:
                    ans = sorted([currentNum,new_arr[j],new_arr[k]])
                    res.add(tuple(ans))
                    j += 1
                    k -= 1
                if currentNum + new_arr[j] + new_arr[k] > 0:
                    k -= 1
                if currentNum + new_arr[j] + new_arr[k] < 0:
                    j += 1
        return [list(x) for x in res]
                

