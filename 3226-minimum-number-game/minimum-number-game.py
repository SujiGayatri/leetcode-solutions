class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0,len(nums),2):
            nums[i:i+2]=nums[i:i+2][::-1]
        return nums