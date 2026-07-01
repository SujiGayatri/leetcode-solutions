class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        n = len(s) // 2
        count1 = 0
        count2 = 0
        for ch in s[:n]:
            if ch in vowels:
                count1 += 1
        for ch in s[n:]:
            if ch in vowels:
                count2 += 1
        return count1 == count2