class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        freq = Counter(hand)
        arr = sorted(hand)
        while arr:
            val = arr.pop(0)
            if freq[val] > 0:
                for x in range(val,val+groupSize):
                    if freq[x] >= 1:
                        freq[x] -= 1
                        if freq[x] == 0:
                            del freq[x]
                    else:
                        return False
            print(freq,'after op',val)
        return True