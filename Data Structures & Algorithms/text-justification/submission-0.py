class Solution:

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        n = len(words)

        curr = []
        ans = []
        currLength = 0

        for i in range(n):

            m = len(words[i])

            if not curr:
                curr.append(words[i])
                currLength += m

            elif currLength + m + 1 <= maxWidth:
                curr.append(words[i])
                currLength += m + 1

            else:
                remain = maxWidth - sum(len(word) for word in curr)
                gaps = len(curr) - 1

                if gaps == 0:
                    line = curr[0] + " " * remain

                else:
                    quo, rem = divmod(remain, gaps)

                    line = ""

                    for j in range(gaps):
                        line += curr[j]

                        space = quo

                        if j < rem:
                            space += 1

                        line += " " * space

                    line += curr[-1]

                ans.append(line)

                curr = [words[i]]
                currLength = m

        # Last line
        line = " ".join(curr)
        line += " " * (maxWidth - len(line))
        ans.append(line)

        return ans