class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted(x * x for x in nums)
        n = len(nums)
        positive = (n + 1) // 2
        return sum(squares[-positive:]) - sum(squares[:-positive])