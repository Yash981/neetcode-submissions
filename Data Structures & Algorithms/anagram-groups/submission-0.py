class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            s1 = "".join(sorted(list(s)))
            hashmap[s1].append(s)
        ans = []
        for k,v in hashmap.items():
            ans.append(v)
        return ans
