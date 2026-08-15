class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        target = math.floor(n/3)
        count1 = 0
        count2 = 0
        currNum1 = 0
        currNum2 = 0
        for i in range(n):
            if count1 == 0 and nums[i] != currNum2:
                count1 = 1
                currNum1 = nums[i]
            elif count2 == 0 and nums[i] != currNum1:
                count2 = 1
                currNum2 = nums[i]
            elif currNum1 == nums[i]:
                count1 += 1
            elif currNum2 == nums[i]:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = 0
        count2 = 0
        res = []
        for i in nums:
            if currNum1 == i:
                count1 += 1
            if currNum2 == i:
                count2 += 1
        if count1 > target:
            res.append(currNum1)
        if count2 > target:
            res.append(currNum2)
        return res 