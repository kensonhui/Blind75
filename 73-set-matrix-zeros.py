class Solution(object):
    def setZeroes(self, matrix):
        """
		not optimal for memory complexity
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(0, m):
            for j in range(0, n):
                if not matrix[i][j]:
                    rows.add(i)
                    cols.add(j)
        for i in rows:
            for j in range(0, n):
                matrix[i][j] = 0
        for i in cols:
            for j in range(0, m):
                matrix[j][i] = 0
        return matrix
