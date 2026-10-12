class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        for shift in range(n):
            rotated = s[shift:] + s[:shift]
            score = 0
            for i in range(n - 1):
                if rotated[i] == rotated[i + 1]:
                    score += 1
            if score == k:
                count += 1
        return count