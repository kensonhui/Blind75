class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 1):
            return 1
        steps = [1 for i in range(0, n)]
        steps[1] = 2
        for i in range(2, n):
            steps[i] = steps[i - 1] + steps[i - 2]
        return steps[n - 1]
        