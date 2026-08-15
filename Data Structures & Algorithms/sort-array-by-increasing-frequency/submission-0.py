class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        arr = []
        freq = Counter(nums)
        for k,v in freq.items():
            arr.append([v,k])
        arr.sort(key=lambda x:(x[0],-x[1]))
        ans = []
        for x,y in arr:
            ans.extend([y]*x)
        return ans