class Solution(object):
    def minPathSum(self, grid):
        m, n = len(grid[0]), len(grid)
        dp = [[1000 for _ in range(m + 1)] for _ in range(n + 1)]
        
        dp[0][1] = 0
        for i in range(n):
            for j in range(m):
                dp[i + 1][j + 1] = min(grid[i][j] + dp[i][j + 1], grid[i][j] + dp[i + 1][j])
        return dp[-1][-1]
