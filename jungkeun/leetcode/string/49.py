class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs = [ (''.join(sorted(s)),s) for s in strs]
        str_map = defaultdict(list)
        for a, s in strs :
            str_map[a].append(s)
        return [s for s in str_map.values()]
