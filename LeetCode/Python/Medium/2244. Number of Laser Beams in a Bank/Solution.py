class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        prev = 0
        ans = 0
        for row in bank:
            devices = row.count('1')
            if devices > 0:
                ans += prev * devices
                prev = devices
        return ans