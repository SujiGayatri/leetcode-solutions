class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        p=zip(heights,names)
        s=sorted(p,reverse=True)
        return [n for h,n in s]