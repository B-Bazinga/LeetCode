class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        # Key: sorted_word , Values: All the words that match upon sorting
        for words in strs:
            sort = tuple(sorted(words))
            group[sort].append(words)
        
        return (list(group.values()))
            





        