class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # 0.记录第一行和第一列是否有0
        first_row_has_zero = any(matrix[0][j]==0 for j in range(n))
        first_col_has_zero = any(matrix[i][0]==0 for i in range(m))

        # 1.利用第一行和第一列做标记，记录出现0的行和列
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        # 2.利用标记，把出第一行第一列外的其他行列置零
        for i in range(1, m):
            for j in range(1, n):
                if(matrix[i][0]==0 or matrix[0][j]==0):
                    matrix[i][j]=0
        # 3.处理第一行和第一列
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j]=0
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0]=0