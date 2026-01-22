class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans=[]
        for i in range(len(matrix[0])):
            new_r=[]
            for j in range(len(matrix)):
                new_r.append(matrix[j][i])
            ans.append(new_r)
        return ans