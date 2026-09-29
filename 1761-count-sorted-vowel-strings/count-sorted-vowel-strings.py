class Solution:
    def countVowelStrings(self, n: int) -> int:
        import math
        return math.comb(n + 4, 4)