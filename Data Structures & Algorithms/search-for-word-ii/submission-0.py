class TrieNode:
    def __init__(self):
        self.children = Counter()
        self.isEndOfWord = False
class Trie:
    def __init__(self):
        self.root =TrieNode()

    def addWord(self, word: str) -> None:
        currNode = self.root
        for c in word:
            if c not in currNode.children:
                currNode.children[c] = TrieNode()
            currNode = currNode.children[c]
        currNode.isEndOfWord = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])
        trie = Trie()
        for word in words:
            trie.addWord(word)
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        ans = []
        def backtrack(i,j,node,curr_word):
            char = board[i][j]
            curr_node = node.children[char]
            if curr_node.isEndOfWord:
                ans.append(curr_word+char)
                curr_node.isEndOfWord  = False
            board[i][j] = '#'
            for d in directions:
                dx = i+d[0]
                dy = j+d[1]
                if 0 <= dx < n and 0 <= dy < m:
                    next_char = board[dx][dy]
                    if next_char in curr_node.children:
                        backtrack(dx,dy,curr_node,curr_word+char)
            board[i][j] = char
        for x in range(n):
            for y in range(m):
                if board[x][y] in trie.root.children:
                    backtrack(x,y,trie.root,"")
        return ans