class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        back_step = 1
        next_step = 2
        swap = 0
        for i in range(2, n):
            swap = next_step
            next_step = next_step + back_step
            back_step = swap
        return next_step
