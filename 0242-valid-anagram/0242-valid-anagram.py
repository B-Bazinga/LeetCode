class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sum_s, sum_t = 0,0
        if len(s) != len(t):
            return False
        # Count the frequency for each character 

        count_char = [0]*26 # Count of each character 

        for i in range (len(s)):
            count_char[ord(s[i])-ord('a')]+=1
            count_char[ord(t[i])-ord('a')]-=1
        
        return all(c==0 for c in count_char)
