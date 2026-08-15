class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        seen = set()
        while num != 1 and num not in seen:
            seen.add(num)
            total = 0
            currNumber = num
            while currNumber:
                rem = currNumber % 10
                total += rem ** 2
                currNumber //= 10
            num = total
        return num==1
