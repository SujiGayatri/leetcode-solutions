class Solution:
    def punishmentNumber(self, n: int) -> int:
        def canPartition(s, target):
            if not s:
                return target == 0
            for j in range(len(s)):
                num = int(s[:j+1])
                if num <= target and canPartition(s[j+1:], target - num):
                    return True

            return False

        total = 0

        for i in range(1, n + 1):
            square = i * i
            if canPartition(str(square), i):
                total += square

        return total