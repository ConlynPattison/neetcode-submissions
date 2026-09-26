class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashed_groups = dict()
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in hashed_groups:
                hashed_groups[sorted_string].append(string)
            else:
                hashed_groups[sorted_string] = [string]

        return list(hashed_groups.values())