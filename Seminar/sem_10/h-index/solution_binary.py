def check(answ, citations):
    total = 0
    for c in citations:
        total += 1 if c >= answ else 0

    return total >= answ

def binary_search(left, right, citations):
    while left <= right:
        mid = (left + right) // 2
        if check(mid, citations):
            answ = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return answ

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return binary_search(0, len(citations), citations)
    