class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = defaultdict(list)
        for i, num in enumerate(nums):
            positions[num].append(i)
        ans = float('inf')
        for j in positions.values():
            if len(j) >= 3:
                for i in range(len(j) - 2):
                    dist = 2 * (j[i+2] - j[i])
                    ans = min(ans, dist)
        return ans if ans != float('inf') else -1