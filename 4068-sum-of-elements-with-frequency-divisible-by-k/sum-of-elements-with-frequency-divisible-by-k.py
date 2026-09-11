class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        ans = 0
        for num, count in freq.items():
            if count % k == 0:
                ans += num * count
        return ans