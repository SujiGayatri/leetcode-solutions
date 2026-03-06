class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = max(nums)
        m = 0
        for num in nums:
            m += max_num - num
        return m