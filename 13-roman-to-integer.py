class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        value = 0
        current = "I"
        for symbol in s[::-1]:
            if lookup[symbol] < lookup[current]:
                value -= lookup[symbol]
            else:
                value += lookup[symbol]
                current = symbol
        return value
