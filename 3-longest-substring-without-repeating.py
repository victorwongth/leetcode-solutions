class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left: int = 0
        right: int = 0
        longest: int = 0
        lookup: Dict[str, int] = {}
        for right in range(len(s)):
            if s[right] not in lookup:
                longest = max(longest, right - left + 1)
            else:
                if lookup[s[right]] < left:
                    longest = max(longest, right - left + 1)
                else:
                    left = lookup[s[right]] + 1
            lookup[s[right]] = right
        return longest
