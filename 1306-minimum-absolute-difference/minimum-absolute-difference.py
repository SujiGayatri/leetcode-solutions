class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff=float('inf')
        ans=[]
        for i in range(len(arr)-1):
            s=arr[i+1]-arr[i]
            if s<min_diff:
                min_diff=s
                ans=[[arr[i],arr[i+1]]]
            elif s==min_diff:
                ans.append([arr[i],arr[i+1]])
        return ans