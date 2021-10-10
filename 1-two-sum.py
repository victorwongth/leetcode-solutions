class Solution;
    def twoSum(self, nums: List[int[, target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            other = target - num
            if other not in lookup:
                lookup[num] = i
            else:
                return [lookup[other], i]
