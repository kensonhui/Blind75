class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1 for i in range(0, len(nums))]
        product = 1
        for i in range(0, len(nums)):
            output[i] = product
            product *= nums[i]
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= product
            product *= nums[i]
        return output
