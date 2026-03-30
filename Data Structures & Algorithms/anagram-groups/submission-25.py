class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            S = ''.join(sorted(s))
            res[S].append(s)
        return list(res.values())