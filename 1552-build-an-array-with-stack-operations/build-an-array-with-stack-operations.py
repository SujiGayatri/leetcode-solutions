class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        result = []
        i = 0
        for num in range(1, n + 1):
            result.append("Push")
            if i < len(target) and num == target[i]:
                i += 1
            else:
                result.append("Pop")
            if i == len(target):
                break
        return result