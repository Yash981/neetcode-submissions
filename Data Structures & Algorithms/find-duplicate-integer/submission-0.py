class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast2 = nums[0]
        while slow != fast2:
            slow = nums[slow]
            fast2 = nums[fast2]
        return slow