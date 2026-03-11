class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)
        ans = [0] * n
        min_cost = float('inf')
        for i in range(n):
            min_cost = min(min_cost, cost[i])
            ans[i] = min_cost
        return ans