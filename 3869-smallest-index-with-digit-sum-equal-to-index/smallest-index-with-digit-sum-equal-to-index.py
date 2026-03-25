class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        smallest_index = -1
        for i in range(len(nums)):
            num_s = str(nums[i])
            digit_sum = 0
            for digit in num_s:
                digit_sum += int(digit)
            if digit_sum == i:
                smallest_index = i
                break  
        return smallest_index