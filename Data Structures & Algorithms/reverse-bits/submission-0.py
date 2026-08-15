class Solution:
    def reverseBits(self, n: int) -> int:
        binOfn = bin(n)[2:].zfill(32)[::-1]
        return int(binOfn,2)