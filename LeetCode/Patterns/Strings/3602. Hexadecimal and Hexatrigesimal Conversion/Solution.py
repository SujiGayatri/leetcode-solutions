class Solution:
    def concatHex36(self, n: int) -> str:
        square = n * n
        cube = n * n * n
        hex_num = format(square, 'X')
        chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while cube > 0:
            result = chars[cube % 36] + result
            cube //= 36
        return hex_num + result