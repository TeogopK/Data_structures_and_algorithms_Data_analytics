def bouquets(t, bloom_days, k):
    bouquets_count = 0
    consecutive = 0
    for days in bloom_days:
        if days <= t:
            consecutive += 1
        else:
            consecutive = 0
        
        if consecutive == k:
            bouquets_count += 1
            consecutive = 0
    
    return bouquets_count
 
def binary_search(left, right, m, k, bloom_days):
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if bouquets(mid, bloom_days, k) < m:
            left = mid + 1
        else:
            ans = mid
            right = mid - 1
            
    return ans
 
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        return binary_search(0, int(1e9), m, k, bloomDay)