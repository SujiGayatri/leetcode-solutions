class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen=set()
        dup=[]
        for i in nums:
            if i in seen:
                dup.append(i)
            seen.add(i)
        return dup
            