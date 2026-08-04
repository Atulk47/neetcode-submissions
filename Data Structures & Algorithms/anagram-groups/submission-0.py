class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res1 = defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s))
            res1[sorteds].append(s)
        return list(res1.values())
        