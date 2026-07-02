class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        return k * mx + (k * (k - 1)) // 2