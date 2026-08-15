class TrieNode:
    def __init__(self):
        self.children = Counter()
        self.isEndOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        if "." not in word:
            node = self.root
            for c in word:
                if c not in node.children:
                    return False
                node = node.children[c]
            return node.isEndOfWord
        else:
            def dfs(i,node):
                if i >= len(word):
                    return node.isEndOfWord
                char = word[i]
                if char == ".":
                    for x in node.children:
                        print(x,word)
                        if dfs(i+1,node.children[x]):
                            return True
                else:
                    if char in node.children:
                        if dfs(i+1,node.children[char]):
                            return True
                return False
            return dfs(0,self.root)
        
