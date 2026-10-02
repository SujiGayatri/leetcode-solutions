class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        weight_map = {}
        for value, weight in items1:
            weight_map[value] = weight_map.get(value, 0) + weight
        
        for value, weight in items2:
            weight_map[value] = weight_map.get(value, 0) + weight
        ret = sorted([[v, w] for v, w in weight_map.items()])
        return ret