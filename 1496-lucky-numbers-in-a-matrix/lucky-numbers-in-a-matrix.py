class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_min = {min(row) for row in matrix}
        col_max = {
            max(matrix[i][j] for i in range(len(matrix)))
            for j in range(len(matrix[0]))
        }
        return list(row_min & col_max)