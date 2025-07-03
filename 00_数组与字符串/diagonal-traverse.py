class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        result = []
        # m+n-1 = 矩阵总对角线个数，count为当前对角线编号
        for count in range(m+n-1):
            temp = []
            # 对角线上的元素的索引和对角线编号的关系：i+j = count
            # 0 <= i <= m-1, 0 <= j <= n-1
            # 也就是0 <= count-i <= n-1
            # 可得 i <= count, i >= count-n+1
            # i的取值范围为：i >= max(0, count-n+1), i <= min(m-1, count)
            start_row = max(0, count-n+1)
            end_row = min(m-1, count)
            for i in range(start_row, end_row+1):
                j = count-i
                # 现在这个顺序是统一从上往下添加元素的
                temp.append(mat[i][j])
            if count%2 == 0:
                # 对角线编号为偶数需要翻转元素
                result.extend(temp[::-1])
            else:
                result.extend(temp)
        return result