class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        output = 0
        digits = 0
        while(n):
            output = (output | (n & 1)) << 1
            digits += 1
            n = n >> 1
        return (output << (32 - digits)) >> 1
