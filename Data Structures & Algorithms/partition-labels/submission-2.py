class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = defaultdict(list)
        for i,x in enumerate(s):
            if x in hashmap:
                if len(hashmap[x]) == 1:
                    hashmap[x].append(i)
                else:
                    hashmap[x][-1] = i
            else:
                hashmap[x].append(i)
        indices = list(hashmap.values())
        stack = [[indices[0][0],indices[0][0]] if len(indices[0])==1 else indices[0]]
        for i in range(1,len(indices)):
            if len(indices[i]) == 1:
                if stack and stack[-1][1] > indices[i][0]:
                    st,en = stack.pop()
                    stack.append([min(st,indices[i][0]),max(en,indices[i][0])])
                    continue
                stack.append([indices[i][0],indices[i][0]])
                continue
            currStart = indices[i][0]
            currEnd = indices[i][1]
            if stack and stack[-1][1] > currStart:
                s,e = stack.pop()
                stack.append([min(s,currStart),max(e,currEnd)])
            else:
                stack.append([currStart,currEnd])
        return [j-i+1 for i,j in stack]


