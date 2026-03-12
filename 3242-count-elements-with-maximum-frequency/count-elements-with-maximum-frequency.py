class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        max_freq = 0
        for i in counts:
            max_freq = max(max_freq, counts[i])
        total_freq = 0
        for num in counts:
            if counts[num] == max_freq:
                total_freq += counts[num]
        return total_freq