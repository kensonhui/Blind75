class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        bitset = [False for i in range(0, n + 1)]
        for i in range(0, n):
            bitset[nums[i]] = True
        for i in range(0, n + 1):
            if not bitset[i]:
                return i
        return n
