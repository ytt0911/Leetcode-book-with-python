class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # 0. 先沿主对角线（左上到右下）转置矩阵
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 1. 再逐行反转矩阵，实现原地旋转
        for i in range(n):
            matrix[i].reverse()