class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        extracted = [i for i in s if i in vowels]
        extracted.sort()
        result = []
        idx = 0
        for j in s:
            if j in vowels:
                result.append(extracted[idx])
                idx += 1
            else:
                result.append(j)
        return ''.join(result)