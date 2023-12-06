class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0

        for c in citations:
            if c >= h + 1:
                h += 1
        
        return h
    