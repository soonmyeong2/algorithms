from collections import deque

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        
        queue, visit = deque([(0, 0)]), set((0, 0))
        while queue:
            x, y = queue.popleft()         
            if x+y == len(s3):
                return True
            if x < len(s1) and s1[x] == s3[x+y] and (x+1, y) not in visit:
                queue.append((x+1, y))
                visit.add((x+1, y))
            if y < len(s2) and s2[y] == s3[x+y] and (x, y+1) not in visit:
                queue.append((x, y+1))
                visit.add((x, y+1))
        return False