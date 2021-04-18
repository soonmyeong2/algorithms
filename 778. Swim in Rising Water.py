import heapq


class Solution(object):
    def swimInWater(self, grid):
        queue, visited, depth = [(grid[0][0], 0, 0)], {(0, 0)}, 0

        while True:
            d, x, y = heapq.heappop(queue)
            depth = max(depth, d)
            if x == y == len(grid) - 1:
                return depth
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < len(grid) and 0 <= ny < len(grid) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heapq.heappush(queue, (grid[nx][ny], nx, ny))
