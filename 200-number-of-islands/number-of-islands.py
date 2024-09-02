class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        islands = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= r or j >= c or grid[i][j] != '1':
                return
            else:
                grid[i][j] = '0'
                dfs(i, j+1) # Right
                dfs(i+1, j) # Down
                dfs(i, j-1) # Left
                dfs(i-1, j) # Up   

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)

        return islands            