class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_num = min(nums)
        max_num = max(nums)
        full = set(range(min_num, max_num + 1))
        nums_set = set(nums)
        missing_val = sorted(list(full - nums_set))
        return missing_val