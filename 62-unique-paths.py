from math import factorial
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return factorial((m - 1) + (n - 1))/(factorial(m - 1)*factorial(n - 1))
