class Solution(object):
    def traverseMemo(self, i, j, visited, m, n, grid1, grid2):
        if (i < 0 or i >= n):
            return True
        if (j < 0 or j >= m):
            return True
        if (visited[i][j]):
            return True
        visited[i][j] = True
        if (grid2[i][j] != 1):
            return True
        
        up = self.traverseMemo(i - 1, j, visited, m, n, grid1, grid2)
        down = self.traverseMemo(i + 1, j, visited, m, n, grid1, grid2)
        left = self.traverseMemo(i, j - 1, visited, m, n, grid1, grid2)
        right = self.traverseMemo(i, j + 1, visited, m, n, grid1, grid2)
        
        return (not (grid2[i][j] == 1 and grid1[i][j] == 0)) and up and down and left and right
                    
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        n = len(grid1)
        m = len(grid1[0])
        visited = [[False for i in range(0, m)] for j in range(0, n)]
        count = 0
        for i in range(0, n):
            for j in range(0, m):
                if (visited[i][j]):
                    continue
                else:
                    if (grid2[i][j] == 1):
                        isIsland = self.traverseMemo(i, j, visited, m, n, grid1, grid2)
                        if (isIsland):
                            count += 1
                    else:
                        visited[i][j] = True
        return count
        
