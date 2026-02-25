class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        n=len(nums)
        m1=float('inf')
        for i in range(len(nums)//2):
            avg=(nums[i]+nums[n-1-i])/2
            m1=min(m1,avg)
        return m1