from typing import List
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            temp = i
            r = 0
            while temp & 1:
                r += 1
                temp >>= 1            
            if r == 0:
                ans.append(-1)
            else:
                ans.append(i - (1 << (r - 1)))       
        return ans