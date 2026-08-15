class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
            x = int(str(x)[1:])
        if x == 0:
            return 0
        ans = []
        while x:
            rem = x % 10
            ans.append(rem)
            x //= 10
        if flag:
            ans.insert(0,'-')
        rev = int("".join(map(str,ans)))

        if -2**31 <= rev <= 2**31-1:
            return rev
        return 0
        
