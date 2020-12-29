class Solution(object):
    def numIslands(self, grid):
        def dfs(x, y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] == '1':
                grid[x][y] = '0'
                list(map(dfs, (x + 1, x - 1, x, x), (y, y, y + 1, y - 1)))

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count