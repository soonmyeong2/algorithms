class Solution(object):
    def isIsomorphic(self, s, t):
        used = set()
        match = dict()
        for i, j in zip(s, t):
            if j not in used and i not in match:
                used.add(j)
                match[i] = j
            if i not in match or match[i] != j:
                return False
        return True
