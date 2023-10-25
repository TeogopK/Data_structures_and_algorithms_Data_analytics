# This will timeout due to O(N^2) time complexity!

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for el in nums:
            if nums.count(el) != 1:
                return True

        return False