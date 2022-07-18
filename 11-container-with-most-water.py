class Solution(object):
    def area(self, height, first, second):
		"""
		:type height: List[int]
		:type first: int
		:type second: int
		rtype: int
		"""
        return abs(first - second) * min(height[first], height[second])
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_volume = 0;
        first = 0
        second = len(height) - 1
        while first < second:
            max_volume = max(max_volume, self.area(height, first, second)) 
            if (height[first] < height[second]):
                first += 1
            else:
                second -= 1
                   
        return max_volume
