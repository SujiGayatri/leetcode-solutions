class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        open_p = 0
        for char in s:
            if char == '(':
                if open_p > 0:
                    res += char
                open_p += 1
            elif char == ')':
                open_p -= 1
                if open_p > 0:
                    res += char
        return res