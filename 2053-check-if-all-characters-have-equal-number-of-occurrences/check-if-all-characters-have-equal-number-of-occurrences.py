class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        f=Counter(s)
        v=list(f.values())
        return all(n==v[0] for n in v)