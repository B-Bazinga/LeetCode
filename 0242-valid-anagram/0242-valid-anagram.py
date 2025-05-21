class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_map = {}

        for i in range(len(s)):
            count_map[s[i]] = count_map.get(s[i],0) + 1
            count_map[t[i]] = count_map.get(t[i],0) - 1

        return all(c==0 for c in count_map.values())
