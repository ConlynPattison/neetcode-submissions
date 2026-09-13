class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate through nums, saving seen and its index
        # if (target-curr) has been seen, respond with indices

        seen = dict()
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
        