class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Only 26 valid, distinct characters that can be input.
        Count in sized array -> cast to immutable tuple -> hash
        and append.
        """
        result = defaultdict(list)

        for string in strs:
            content = [0] * 26
            
            for char in string:
                content[ord(char) - ord("a")] += 1
            
            result[tuple(content)].append(string)

        return list(result.values())