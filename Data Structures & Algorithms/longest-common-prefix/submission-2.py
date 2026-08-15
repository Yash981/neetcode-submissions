class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mn = min([len(i) for i in strs])
        ans = ""
        for x in range(mn):
            curr = set()
            for y in range(len(strs)):
                if not strs[y]:
                    return ""
                curr.add(strs[y][x])
            if len(curr) == 1:
                ans += strs[0][x]
            else:
                return ans
        return ans
            