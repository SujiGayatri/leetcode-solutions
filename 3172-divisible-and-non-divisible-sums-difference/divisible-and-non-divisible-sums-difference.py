class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        k = n // m
        num2 = m * k * (k + 1) // 2
        num1 = total - num2
        return num1 - num2