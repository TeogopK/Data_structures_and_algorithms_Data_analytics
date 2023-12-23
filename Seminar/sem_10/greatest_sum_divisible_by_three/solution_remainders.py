class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        remainders = [
            [],
            [],
            []
        ]
 
        for num in nums:
            remainders[num % 3].append(num)
 
        remainders[1].extend([int(1e9), int(1e9)])
        remainders[2].extend([int(1e9), int(1e9)])
 
        remainders[1].sort()
        remainders[2].sort()
 
        ans = sum(nums)
 
        if ans % 3 == 1:
            ans = ans - min(remainders[1][0], remainders[2][0] + remainders[2][1])
        elif ans % 3 == 2:
            ans = ans - min(remainders[2][0], remainders[1][0] + remainders[1][1])
 
        return max(ans, 0)