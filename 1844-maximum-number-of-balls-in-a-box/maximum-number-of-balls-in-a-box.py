class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box_counts = [0] * 46
        max_balls = 0
        for ball in range(lowLimit, highLimit + 1):
            digit_sum = 0
            temp = ball
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
            box_counts[digit_sum] += 1
            if box_counts[digit_sum] > max_balls:
                max_balls = box_counts[digit_sum]
                
        return max_balls