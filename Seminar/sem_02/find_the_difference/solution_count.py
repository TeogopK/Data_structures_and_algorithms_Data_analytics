# O(N^2) time complexity worst case

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for ch in t:
            if s.count(ch) != t.count(ch):
                return ch