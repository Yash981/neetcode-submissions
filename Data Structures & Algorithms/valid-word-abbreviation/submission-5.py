class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n = len(word)
        m = len(abbr)
        i = 0
        j = 0
        while i < n and j < m:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit():
                x = []
                while j < m and abbr[j].isdigit():
                    x.append(abbr[j])
                    j += 1
                j -= 1
                if x[0] == "0":
                    return False
                newx = "".join(x)
                newx = int(newx)
                while newx > 0 and i < n:
                    i += 1
                    newx -= 1
                if newx > 0:
                    return False
                j += 1
            else:
                return False
        if i == n and j == m:
            return True
        return False