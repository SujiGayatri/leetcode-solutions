class Solution:
    def findLucky(self, arr: list[int]) -> int:
        frequency = {}
        for num in arr:
            frequency[num] = frequency.get(num, 0) + 1
        lucky = -1
        for num, count in frequency.items():
            if num == count:
                lucky = max(lucky, num)
        return lucky