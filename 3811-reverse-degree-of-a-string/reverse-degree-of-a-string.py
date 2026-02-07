class Solution:
    def reverseDegree(self, s: str) -> int:
        totalS = 0
        for i, ch in enumerate(s):
            reversed_value = 26 - (ord(ch) - ord('a'))
            totalS += reversed_value * (i + 1)
        return totalS