class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')
        for ls, ld in zip(landStartTime, landDuration):
            for ws, wd in zip(waterStartTime, waterDuration):
                land_finish = ls + ld
                finish1 = max(ws, land_finish) + wd
                water_finish = ws + wd
                finish2 = max(ls, water_finish) + ld
                ans = min(ans, finish1, finish2)
        return ans