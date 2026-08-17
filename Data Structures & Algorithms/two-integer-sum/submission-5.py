class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in hsh:
                return [hsh[diff], i]
            hsh[x] = i