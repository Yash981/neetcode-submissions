class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        indegree = [0] * 26
        graph = defaultdict(list)
        all_chars = set()
        for word in words:
            for c in word:
                all_chars.add(c)
        n = len(words)
        for i in range(n-1):
            f = words[i]
            s = words[i+1]
            m = min(len(f),len(s))
            if len(f) > len(s) and f[:m] == s[:m]:
                return ""
            x = 0
            y = 0
            while x < m and y < m:
                if f[x] != s[y]:
                    graph[f[x]].append(s[y])
                    indegree[ord(s[y])-ord('a')] += 1
                    break
                x += 1
                y += 1
        queue = deque([c for c in all_chars if indegree[ord(c)-97] == 0])

        # print(graph)
        # print(indegree)
        ans = ""
        while queue:
            node = queue.popleft()
            ans += node
            for neighbour in graph[node]:
                indegree[ord(neighbour)-ord('a')] -= 1
                if indegree[ord(neighbour)-ord('a')] == 0:
                    queue.append(neighbour)
        if len(ans) != len(all_chars):
            return ""
        return ans
            

            

