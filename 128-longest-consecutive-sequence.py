class Solution:
    def __init__(self) -> None:
        self.longest: int = 0
        self.seen: Set[int] = set()

    def longestConsecutive(self, nums: List[int]) -> int:
        self.nums: Set[int] = set(nums)
        if len(nums) == 0:
            return 0

        for num in self.nums:
            if num not in self.seen:
                self.seen.add(num)
                length = 1
                length += self._checkUpperAdjacent(num + 1)
                length += self._checkLowerAdjacent(num - 1)
                if length > self.longest:
                    self.longest = length
        return self.longest

    def _checkUpperAdjacent(self, num: int) -> int: 
        if num in self.seen:
            return 0
        if num not in self.nums:
            return 0
        self.seen.add(num)
        return 1 + self._checkUpperAdjacent(num + 1)
        
    def _checkLowerAdjacent(self, num: int) -> int:
        if num in self.seen:
            return 0
        if num not in self.nums:
            return 0
        self.seen.add(num)
        return 1 + self._checkLowerAdjacent(num - 1)
    
    
    
# Better solution to skip if (num - 1) in set
def longestConsecutive(self, nums):
    nums = set(nums)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
    return best
