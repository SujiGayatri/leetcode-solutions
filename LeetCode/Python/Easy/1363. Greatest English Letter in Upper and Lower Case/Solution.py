class Solution:
    def greatestLetter(self, s: str) -> str:
        letters = set(s)
        for ch in reversed("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            if ch in letters and ch.lower() in letters:
                return ch
        return ""