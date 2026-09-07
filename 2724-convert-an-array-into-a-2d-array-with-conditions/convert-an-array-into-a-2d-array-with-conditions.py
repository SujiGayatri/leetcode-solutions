class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        freq = Counter(nums)
        result = [[] for _ in range(max(freq.values()))]
        for num, count in freq.items():
            for i in range(count):
                result[i].append(num)

        return result