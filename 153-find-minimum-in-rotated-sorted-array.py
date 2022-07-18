class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (nums[0] < nums[-1]):
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if (nums[middle] > nums[right]):
                left = middle + 1
            else:
                right = middle
        return nums[left]

