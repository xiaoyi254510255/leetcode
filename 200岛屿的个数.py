class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        
        direct = [[0,1], [1,0], [0,-1], [-1,0]]
        
        def inArea(x, y):
            return (x >= 0) and (x < m) and (y >= 0) and (y < n)
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        res = 0
        
        def dfs(grid, x , y):
            visited[x][y] = True
            for i in range(4):
                newx = x + direct[i][0]
                newy = y + direct[i][1]
                
                if inArea(newx, newy) and (not visited[newx][newy]) and (grid[newx][newy] == '1'):
                    dfs(grid, newx, newy)
            return 
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == '1' and (not visited[i][j])):
                    res += 1
                    dfs(grid, i , j)
                
        return res
