class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        start = 0
        n = len(digits)
        for i in range(n):
            start = (start << 3) + (start << 1) + digits[i]
        res = start+1
        ans = []
        while res:
            lastdigit = res % 10
            ans.append(lastdigit)
            res //= 10
        return ans[::-1]


