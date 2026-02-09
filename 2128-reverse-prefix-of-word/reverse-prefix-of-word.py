class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        r=""
        found=False
        for i in range(len(word)):
            r+=word[i]
            if word[i]==ch:
                word=word[i+1:]
                found=True
                break
        if not found:
            return word
        r=r[::-1]
        r+=word
        return r