class Solution:
    def countDigits(self, num: int) -> int:
        cnt = 0
        num_str = str(num)
        for digit in num_str:
            digit = int(digit)
            if digit != 0 and num % digit == 0:
                cnt += 1
        return cnt