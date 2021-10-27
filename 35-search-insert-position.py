class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            index = (high + low) // 2
            if target == nums[index]:
                 return index 
            else:
                if target < nums[index]:
                    high = index
                else:
                    low = index + 1
                    
        if target > nums[low]:
            return low + 1
        else:
            return low
