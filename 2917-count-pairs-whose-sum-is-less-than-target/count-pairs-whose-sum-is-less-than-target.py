class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        nums.sort()
        cnt=0
        while l<r:
            s=nums[l]+nums[r]
            if s<target:
                cnt+=(r-l)
                l+=1
            else:
                r-=1
        return cnt