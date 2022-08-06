class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascals_triangle = [[1]]
        for i in range(0, numRows - 1):
            new_row = [1]
            for j in range(0, i):
                new_row.append(pascals_triangle[i][j] + pascals_triangle[i][j + 1])
            new_row.append(1)
            pascals_triangle.append(new_row)
        return pascals_triangle
