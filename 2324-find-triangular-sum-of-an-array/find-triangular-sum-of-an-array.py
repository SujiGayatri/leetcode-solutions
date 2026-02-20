class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            res=[]
            for j in range(len(nums)-1):
                s=(nums[j]+nums[j+1])%10
                res.append(s)
            nums=res
        return nums[0]