from sortedcontainers import SortedList
class Solution:
    def reorganizeString(self, s: str) -> str:
        hp = SortedList([[y,x] for x,y in Counter(s).items()])
        # print(hp)
        ans = []
        while len(hp) > 1:
            val1,key1 = hp.pop()
            val2,key2 = hp.pop()
            ans.append(key1)
            ans.append(key2)
            val1 -= 1
            val2 -= 1
            if val1 > 0:
                hp.add([val1,key1])
            if val2 > 0:
                hp.add([val2,key2])
        if hp and hp[0][0] > 1:
            return ""
        if hp:
            ans.append(hp[0][1])
        return "".join(ans)