class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        max_range = -1
        for num in nums:
            digits = [int(d) for d in str(num)]
            digit_range = max(digits) - min(digits)
            max_range = max(max_range, digit_range)
        ans = 0
        for num in nums:
            digits = [int(d) for d in str(num)]
            digit_range = max(digits) - min(digits)

            if digit_range == max_range:
                ans += num
        return ans