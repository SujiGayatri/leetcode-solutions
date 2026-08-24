class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_s=set(nums)
        ans=0
        for num in nums_s:
            if (num-1) not in nums_s:
                current_num=num
                current_sum=1
                while (current_num+1) in nums_s:
                    current_num+=1
                    current_sum+=1
                ans=max(ans,current_sum)
        return ans