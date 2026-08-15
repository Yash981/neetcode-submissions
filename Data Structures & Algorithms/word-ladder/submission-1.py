class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        queue = deque([(beginWord,1)])
        while queue:
            word,times = queue.popleft()
            if word == endWord:
                return times
            for i in range(len(word)):
                for j in range(26):
                    nextWord = word[:i] + chr(97+j) + word[i+1:]
                    if nextWord in wordSet:
                        wordSet.remove(nextWord)
                        queue.append((nextWord,times+1))
        return 0

