class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        current = ""
        for ch in target:
            current += 'a'
            ans.append(current)
            for c in range(ord('a') + 1, ord(ch) + 1):
                current = current[:-1] + chr(c)
                ans.append(current)
        return ans