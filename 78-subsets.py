class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_set = 2 ** (len(nums))
        
        super_set = []
        for i in range(0, nums_set):
            subset = []
            for j in range(0, len(nums)):
                if ((i >> j) & 1):
                    subset.append(nums[j])
            super_set.append(subset)
        
        return super_set