# O(N) time complexity
import string

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1 = {symb: 0 for symb in string.ascii_lowercase}
        d2 = d1.copy()

        for ch in s:
            d1[ch] += 1

        for ch in t:
            d2[ch] += 1
        
        for symb in string.ascii_lowercase:
            if d1[symb] != d2[symb]:
                return symb