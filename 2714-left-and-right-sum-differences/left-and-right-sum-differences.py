class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        leftSum=0
        total=sum(nums)
        for i in range(n):
            rightSum=total-leftSum-nums[i]
            res[i]=abs(leftSum-rightSum)
            leftSum+=nums[i]
        return res