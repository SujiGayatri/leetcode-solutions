class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n + 1) // 2
        for x in range(1, n + 1):
            left_sum = x * (x + 1) // 2
            right_sum = total - (x * (x - 1) // 2)
            if left_sum == right_sum:
                return x
        return -1