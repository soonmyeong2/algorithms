from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans, fresh = 0, 0
        queue = deque()
        for y, row in enumerate(grid):
            for x, value in enumerate(row):
                if value == 2:
                    queue.append((x, y, 0))
                if value == 1:
                    fresh += 1       
        while queue:
            x, y, time = queue.popleft()
            ans = max(ans, time)
            for dx, dy in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid) and grid[y+dy][x+dx] == 1:
                    fresh -= 1
                    grid[y+dy][x+dx] = 2
                    queue.append((x+dx, y+dy, time+1))
        return ans if not fresh else -1