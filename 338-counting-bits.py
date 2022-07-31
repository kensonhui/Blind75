class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if (n == 0):
            return [0]
        count = 0
        power = 1
        output = [0 for i in range(0, n + 1)]
        output[1] = 1
        for i in range(2, n + 1):
            if (i >> power >= 2):
                power += 1
            output[i] = output[i - (2**power)] + 1
        return output
