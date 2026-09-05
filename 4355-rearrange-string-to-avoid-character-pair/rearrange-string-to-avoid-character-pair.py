class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        return ''.join(c for c in s if c == y) + \
           ''.join(c for c in s if c != x and c != y) + \
           ''.join(c for c in s if c == x)