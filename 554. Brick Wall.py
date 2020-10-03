from collections import defaultdict

class Solution(object):
    def leastBricks(self, wall):
        counter = defaultdict(int)
        for row in wall:
            for i in range(1, len(row)):
                row[i] += row[i-1]
                counter[row[i-1]] += 1
        return len(wall) - max(counter.values() + [0])