class Solution:
    def isValid(self, s: str) -> bool:
        expect = []
        match = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for char in s:
            if char in match.keys():
                expect.append(match[char])
            elif expect == [] or char != expect.pop():
                return False
        return expect == []
