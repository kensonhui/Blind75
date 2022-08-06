class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        def floodFillColor(image, sr, sc, color, start_color):
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
                return
            if image[sr][sc] != start_color:
                return
            image[sr][sc] = color
            floodFillColor(image, sr + 1, sc, color, start_color)
            floodFillColor(image, sr - 1, sc, color, start_color)
            floodFillColor(image, sr, sc + 1, color, start_color)
            floodFillColor(image, sr, sc - 1, color, start_color)
        if color != image[sr][sc]:
            floodFillColor(image, sr, sc, color, image[sr][sc])
        return image
