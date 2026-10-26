class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        max_cost = max(costs)
        count = [0] * (max_cost + 1)
        for cost in costs:
            count[cost] += 1
        bought = 0
        for price in range(1, max_cost + 1):
            if count[price] == 0:
                continue
            can_buy = min(count[price], coins // price)
            bought += can_buy
            coins -= can_buy * price
            if coins < price:
                break
        return bought