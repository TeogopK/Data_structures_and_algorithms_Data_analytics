# O(NlogN) time complexity

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        
        return t[-1]