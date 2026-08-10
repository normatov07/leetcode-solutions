class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramMap = defaultdict(list)

        for st in strs:
            anagramMap["".join(sorted(st))].append(st)
        
        result = []

        for part in anagramMap.values():
            result.append(part)
        
        return result

