# Sorts the list into a new list .
# Then, starts searching for pairs from both ends.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)

        i, j = 0, len(nums) - 1

        while i < j:
            if sorted_nums[i] + sorted_nums[j] > target:
                j -= 1
            elif sorted_nums[i] + sorted_nums[j] < target:
                i += 1
            else:
                orig_i = nums.index(sorted_nums[i])
                orig_j = len(nums) - 1 - nums[::-1].index(sorted_nums[j]) # avoids nums = [3, 3]
                return [orig_i, orig_j]