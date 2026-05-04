from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        steps = 0
        for c in count_t:
            if count_t[c] > count_s[c]:
                steps += count_t[c] - count_s[c]
        return steps  