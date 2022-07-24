class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        tallest = 0
        water = 0
        maxy = [0 for i in height]
        for i in range(len(height) - 1, -1, -1):
            maxy[i] = tallest
            tallest = max(height[i], tallest)
        tallest = 0
        for j in range(0, len(height)):
            water += max(min(tallest, maxy[j]) - height[j], 0)
            tallest = max(tallest, height[j])
            
        return water
