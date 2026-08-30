import bisect
from functools import lru_cache
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        print(envelopes)
        env = [y for _,y in envelopes]
        n = len(envelopes)
        arr = [env[0]]
        for i in range(1,n):
            if arr[-1] < env[i]:
                arr.append(env[i])
            else:
                index = bisect.bisect_left(arr,env[i])
                arr[index] = env[i]
        return len(arr)
            
            
            